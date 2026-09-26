# Data exploration
### 2022_oct
```sh
$ head -2 data_2022_oct.csv 
event_time,event_type,product_id,price,user_id,user_session
2022-10-01 00:00:00 UTC,cart,5773203,2.62,463240011,26dd6e6e-4dac-4778-8d2c-92e149dab885

$tail -n +2  data_2022_oct.csv | wc -l
4102283
$ { head -1 data_2022_oct.csv | cut -d, -f2; tail -n +2 data_2022_oct.csv | cut -d, -f2 | grep -v '^[[:space:]]*$' | wc -l; }
event_type
4102283
$ { head -1 data_2022_oct.csv | cut -d, -f3; tail -n +2 data_2022_oct.csv | cut -d, -f3 | grep -v '^[[:space:]]*$' | wc -l; }
product_id
4102283
$ { head -1 data_2022_oct.csv | cut -d, -f4; tail -n +2 data_2022_oct.csv | cut -d, -f4 | grep -v '^[[:space:]]*$' | wc -l; }
price
4102283
$ { head -1 data_2022_oct.csv | cut -d, -f5; tail -n +2 data_2022_oct.csv | cut -d, -f5 | grep -v '^[[:space:]]*$' | wc -l; }
user_id
4102283
$ { head -1 data_2022_oct.csv | cut -d, -f6; tail -n +2 data_2022_oct.csv | cut -d, -f6 | grep -v '^[[:space:]]*$' | wc -l; }
user_session
4101646  <=== hay vacios.

$  tail -n +2 data_2022_oct.csv | cut -d, -f2 | sort | uniq -c
1232385 cart
 245624 purchase
 762110 remove_from_cart
1862164 view
```

### 2022_nov
```sh
$ head -2 data_2022_nov.csv 
event_time,event_type,product_id,price,user_id,user_session
2022-11-01 00:00:02 UTC,view,5802432,0.32,562076640,09fafd6c-6c99-46b1-834f-33527f4de241

$ tail -n +2  data_2022_nov.csv | wc -l
4635837
$ { head -1 data_2022_nov.csv | cut -d, -f1; tail -n +2 data_2022_nov.csv | cut -d, -f1 | grep -v '^[[:space:]]*$' | wc -l; }
event_time
4635837
$ { head -1 data_2022_nov.csv | cut -d, -f2; tail -n +2 data_2022_nov.csv | cut -d, -f2 | grep -v '^[[:space:]]*$' | wc -l; }
event_type
4635837
$ { head -1 data_2022_nov.csv | cut -d, -f3; tail -n +2 data_2022_nov.csv | cut -d, -f3 | grep -v '^[[:space:]]*$' | wc -l; }
product_id
4635837
$ { head -1 data_2022_nov.csv | cut -d, -f4; tail -n +2 data_2022_nov.csv | cut -d, -f4 | grep -v '^[[:space:]]*$' | wc -l; }
price
4635837
$ { head -1 data_2022_nov.csv | cut -d, -f5; tail -n +2 data_2022_nov.csv | cut -d, -f5 | grep -v '^[[:space:]]*$' | wc -l; }
user_id
4635837
$ { head -1 data_2022_nov.csv | cut -d, -f6; tail -n +2 data_2022_nov.csv | cut -d, -f6 | grep -v '^[[:space:]]*$' | wc -l; }
user_session
4635024 <=== Hay vacios

$  tail -n +2 data_2022_nov.csv | cut -d, -f2 | sort | uniq -c
1311807 cart
 322417 purchase
 925481 remove_from_cart
2076132 view
```

### 2022_dic
```sh
$ head -2 data_2022_dec.csv 
event_time,event_type,product_id,price,user_id,user_session
2022-12-01 00:00:00 UTC,remove_from_cart,5712790,6.27,576802932,51d85cb0-897f-48d2-918b-ad63965c12dc

$ tail -n +2  data_2022_dec.csv | wc -l
3533286
$ { head -1 data_2022_dec.csv | cut -d, -f1; tail -n +2 data_2022_dec.csv | cut -d, -f1 | grep -v '^[[:space:]]*$' | wc -l; }
event_time
3533286
$ { head -1 data_2022_dec.csv | cut -d, -f2; tail -n +2 data_2022_dec.csv | cut -d, -f2 | grep -v '^[[:space:]]*$' | wc -l; }
event_type
3533286
$ { head -1 data_2022_dec.csv | cut -d, -f3; tail -n +2 data_2022_dec.csv | cut -d, -f3 | grep -v '^[[:space:]]*$' | wc -l; }
product_id
3533286
$ { head -1 data_2022_dec.csv | cut -d, -f4; tail -n +2 data_2022_dec.csv | cut -d, -f4 | grep -v '^[[:space:]]*$' | wc -l; }
price
3533286
$ { head -1 data_2022_dec.csv | cut -d, -f5; tail -n +2 data_2022_dec.csv | cut -d, -f5 | grep -v '^[[:space:]]*$' | wc -l; }
user_id
3533286
$ { head -1 data_2022_dec.csv | cut -d, -f6; tail -n +2 data_2022_dec.csv | cut -d, -f6 | grep -v '^[[:space:]]*$' | wc -l; }
user_session
3532507 <=== Hay vacios

$  tail -n +2 data_2022_dec.csv | cut -d, -f2 | sort | uniq -c
 927124 cart
 213176 purchase
 664655 remove_from_cart
1728331 view
```

### 2023_jan
```sh
$ head -2 data_2023_jan.csv 
event_time,event_type,product_id,price,user_id,user_session
2023-01-01 00:00:00 UTC,view,5809910,5.24,595414620,4adb70bb-edbd-4981-b60f-a05bfd32683a

$ tail -n +2  data_2023_jan.csv | wc -l
4264752
$ { head -1 data_2023_jan.csv | cut -d, -f1; tail -n +2 data_2023_jan.csv | cut -d, -f1 | grep -v '^[[:space:]]*$' | wc -l; }
event_time
4264752
$ { head -1 data_2023_jan.csv | cut -d, -f2; tail -n +2 data_2023_jan.csv | cut -d, -f2 | grep -v '^[[:space:]]*$' | wc -l; }
event_type
4264752
$ { head -1 data_2023_jan.csv | cut -d, -f3; tail -n +2 data_2023_jan.csv | cut -d, -f3 | grep -v '^[[:space:]]*$' | wc -l; }
product_id
4264752
$ { head -1 data_2023_jan.csv | cut -d, -f4; tail -n +2 data_2023_jan.csv | cut -d, -f4 | grep -v '^[[:space:]]*$' | wc -l; }
price
4264752
$ { head -1 data_2023_jan.csv | cut -d, -f5; tail -n +2 data_2023_jan.csv | cut -d, -f5 | grep -v '^[[:space:]]*$' | wc -l; }
user_id
4264752
$ { head -1 data_2023_jan.csv | cut -d, -f6; tail -n +2 data_2023_jan.csv | cut -d, -f6 | grep -v '^[[:space:]]*$' | wc -l; }
user_session
4263438 <=== Hay vacios
$  tail -n +2 data_2023_jan.csv | cut -d, -f2 | sort | uniq -c
1148323 cart
 263797 purchase
 815024 remove_from_cart
2037608 view
```

# Table Creation

## First try

```sql
        CREATE TABLE IF NOT EXISTS {} (
            event_time   TIMESTAMPTZ   NOT NULL,
            event_type   TEXT          NOT NULL
                        CHECK (event_type IN ('view', 'cart', 'purchase', 'remove_from_cart')),
            product_id   INTEGER       NOT NULL,
            price        NUMERIC(8,2)  NOT NULL,
            user_id      BIGINT       NOT NULL,
            user_session UUID          NOT NULL
        );
```


```sql
piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2022_oct'));
 pg_size_pretty 
----------------
 313 MB
(1 row)

piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2022_nov'));
 pg_size_pretty 
----------------
 355 MB
(1 row)

piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2022_dec'));
 pg_size_pretty 
----------------
 290 MB
(1 row)

piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2023_jan'));
 pg_size_pretty 
----------------
 326 MB
(1 row)
```
## Second try


```sql
piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2022_oct'));
 pg_size_pretty 
----------------
 299 MB
(1 row)

piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2022_nov'));
 pg_size_pretty 
----------------
 338 MB
(1 row)

piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2022_dec'));
 pg_size_pretty 
----------------
 258 MB
(1 row)

piscineds=# SELECT pg_size_pretty(pg_relation_size('data_2023_jan'));
 pg_size_pretty 
----------------
 311 MB
(1 row)

```

## Third Try

|table        | text  |type_evert_t|Saving 1 | % 1   |columns order|
|-------------|-------|------------|---------|-------|-------------|
|data_2022_oct| 313 MB| 299 MB     |14 MB    | 4.47 %||
|data_2022_nov| 355 MB| 338 MB     |17 MB    | 4.78 %||
|data_2022_dec| 290 MB| 258 MB     |32 MB    |11.05 %||
|data_2023_jan| 326 MB| 311 MB     |15 MB    | 4.60 %||
|**total**    |1284 MB|1206 MB     |78 MB    | 6,07 %||