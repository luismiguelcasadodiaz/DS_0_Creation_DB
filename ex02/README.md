# 2022_oct
```sh
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
```

# 2022_nov
```sh
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
```

# 2022_dic
```sh
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
```

# 2023_jan
```sh
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
```