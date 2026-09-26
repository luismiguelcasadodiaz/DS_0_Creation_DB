# Data exploration

## Rows
```sh
tail -n +2 item.csv | wc -l
109579
```

## Features
```sh
head -2 item.csv 
product_id,category_id,category_code,brand
5712790,1487580005268456192,,f.o.x
```

### Product_id 
There are 54,043 distinct `product_id` values, ranging from 3,752 to  5,932,595. These values fit within the PostgreSQL 18 INTEGER data type. All records have a value, butthe column cannot be a primary key becasue the values are not unique.

```sh
cat  item.csv | cut -d, -f1 | sort | uniq | wc -l
54044
cat  item.csv | cut -d, -f1 | sort -n| uniq | sed -n '1p;2p;$p'
product_id
3752
5932595
{ head -1 item.csv | cut -d, -f1; tail -n +2 item.csv | cut -d, -f1 | grep -v '^[[:space:]]*$' | wc -l; }
product_id
109579
```

### Category_id
There are 522 distinct `category_id` values, ranging from 1487580004807082752 to 2242903426784559104. These values fit within the Postgresql18 BIGINT datatype. Of the 109579 records, 41899 records have no Categroy_id value.

```
cat  item.csv | cut -d, -f2 | sort | uniq | wc -l
524
{ head -1 item.csv | cut -d, -f2; tail -n +2 item.csv | cut -d, -f2 | grep -v '^[[:space:]]*$' | sort -nu | sed -n '1p;$p'; }
category_id
1487580004807082752
2242903426784559104
{ echo "lines with no value"; cut -d, -f2 item.csv  | grep -c '^[[:space:]]*$'; }
lines with no value
41899
```

### Category_code
There are only 12 distinct `category_code` values. Subcategories exists. Of the 109579 records, 108769 records have no Category_id value

```sh
(piscine) ~/ds/DS_0_Creation_DB/data/item $ { head -1 item.csv | cut -d, -f3; tail -n +2 item.csv | cut -d, -f3 | grep -v '^[[:space:]]*$' | sort -u | cat -n; }
category_code
     1  accessories.bag
     2  accessories.cosmetic_bag
     3  apparel.glove
     4  appliances.environment.air_conditioner
     5  appliances.environment.vacuum
     6  appliances.personal.hair_cutter
     7  appliances.personal.massager
     8  furniture.bathroom.bath
     9  furniture.living_room.cabinet
    10  furniture.living_room.chair
    11  sport.diving
    12  stationery.cartrige
{ echo "lines with no value"; cut -d, -f3 item.csv  | grep -c '^[[:space:]]*$'; }
lines with no value
108769
```

```sql
piscineds=# SELECT category_code, count(*) FROM items GROUP BY category_code ORDER BY Category_code;
             category_code              | count  
----------------------------------------+--------
 accessories.bag                        |     45
 accessories.cosmetic_bag               |     28
 apparel.glove                          |    165
 appliances.environment.air_conditioner |     33
 appliances.environment.vacuum          |    125
 appliances.personal.hair_cutter        |     57
 appliances.personal.massager           |     91
 furniture.bathroom.bath                |     89
 furniture.living_room.cabinet          |      7
 furniture.living_room.chair            |      2
 sport.diving                           |      1
 stationery.cartrige                    |    167
                                        | 108769
```                                        

### Brand
There are only 273 distinct `brand` values. Of the 109,579 records, 77,795 records have no Categroy_id value.


## Table Creation
My first approach i declared the fields in the order they appear in the CSV.

```sql
        CREATE TABLE IF NOT EXISTS {} (
            product_id    INTEGER NOT NULL,            
            category_id   BIGINT,        
            category_code TEXT,
            brand         TEXT);
```
After importing the data, the table size was of `5,032KB`
```sql
SELECT pg_size_pretty(pg_relation_size('items'));
```



PostgreSQL requires every value to start at a byte offset that is a multiple of its type's alignment, and BIGINT has an 8-byte alignment.

```sql
SELECT typname, typlen, typalign FROM pg_type WHERE typname IN ('int2', 'int4', 'int8', 'date', 'timestamp', 'text', 'bool', 'bigint');
  typname  | typlen | typalign 
-----------+--------+----------
 bool      |      1 | c
 int8      |      8 | d
 int2      |      2 | s
 int4      |      4 | i
 text      |     -1 | i
 date      |      4 | i
 timestamp |      8 | d
(7 rows)
```
In the typalign column, c means 1 byte, s means 2 bytes, i means 4 bytes, and d means 8 bytes.

After product_id fills bytes 0–3, the next free byte is 4. But 4 is not a multiple of 8, so category_id can't start there. The next valid position is byte 8, and bytes 4–7 are left empty as padding:
```text
offset:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
        [ product_id  ][   padding     ][         category_id          ]
```

        

With BIGINT first, no gap is needed, because offset 8 is already a multiple of 4:

```text
offset:  0   1   2   3   4   5   6   7   8   9  10  11
        [         category_id          ][ product_id  ]
```


Why PostgreSQL does this: CPUs read memory most efficiently when an 8-byte value sits at an address divisible by 8. On some processors a misaligned read is slower; on others it can crash the program. PostgreSQL reads rows directly from the disk page loaded into memory, without converting them first, so the on-disk layout has to already match what the CPU needs. The row's data area itself also starts at an aligned offset (the 23-byte header is padded to 24), so an offset of 8 inside the row really does land on an 8-byte boundary in memory.

So if the row had only these two columns (or the text columns were NULL), both orders would take exactly the same space. The padding just moves from the middle to the end.

Where the reordering actually helps is when something follows. Your TEXT columns don't need alignment when short, so with category_id, product_id the text can start right at byte 12 and use those 4 bytes, instead of the 4 bytes being wasted as internal padding:

```text
product_id first:   [ product_id ][ padding ][ category_id ][ text... ]  text starts at 16
category_id first:  [ category_id ][ product_id ][ text... ]             text starts at 12
``` 
Then the whole row is rounded up to a multiple of 8 at the end. That's why I said earlier the saving per row is either 8 bytes or 0, depending on the text lengths, and averages about 4.

Konowing this i permutted numeric fields:

```sql
        CREATE TABLE IF NOT EXISTS {} (
            category_id   BIGINT,        
            product_id    INTEGER NOT NULL,
            category_code TEXT,
            brand         TEXT);
```

After importing the data, the table size was of `4,904KB`. I saved 2,54%.
```sql
SELECT pg_size_pretty(pg_relation_size('items'));
```

