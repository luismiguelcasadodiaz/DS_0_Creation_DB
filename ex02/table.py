import psycopg
import sys
import os


def path_test(path: str) -> str:
    """Validate that a given path points to a readable CSV/TXT/JSON file.

    Resolves the provided path to an absolute path and runs a series of
    checks to ensure the file exists, is a regular file (not a directory),
    is readable by the current user, and has a .csv, .txt, or .json extension.

    Args:
        path: A relative or absolute filesystem path to validate.

    Returns:
        The resolved absolute path to the validated CSV, TXT, or JSON file.

    Raises:
        AssertionError: If the path does not exist, is not a regular file,
            is not readable, or does not have a .csv/.txt/.json extension.
    """
    abspath = os.path.abspath(path)
    assert os.path.exists(abspath), f"Wrong Path {path}"
    assert os.path.isfile(abspath), f"{path} is not a file"
    assert os.access(abspath, os.R_OK), f"User can not read permit on {path}"
    _, ext = os.path.splitext(abspath)
    assert ext.lower() in (".csv", ".json", ".txt"), \
        f"Expected a CSV file, got '{ext[1:]}'"
    return abspath


def main(table_path: str):
    basename = os.path.basename(table_path)
    tablename = os.path.splitext(basename)[0]
    sql0 = "SELECT EXISTS (SELECT 1 FROM information_schema.tables "
    sql0 += f"WHERE table_schema = 'public' AND table_name = '{tablename}');"

    sql1 = f"CREATE TABLE IF NOT EXISTS {tablename} ("
    sql1 +=       "event_time   TIMESTAMPTZ NOT NULL,"
    sql1 +=       "event_type   TEXT NOT NULL CHECK (event_type IN ('view',"
    sql1 +=       "                                                   'cart',"
    sql1 +=       "                                                   'purchase',"
    sql1 +=       "                                                   'remove_from_cart')),"
    sql1 +=       "product_id   INTEGER NOT NULL,"
    sql1 +=       "price        NUMERIC(8,2) NOT NULL,"
    sql1 +=       "user_id      INTEGER NOT NULL,"
    sql1 +=       "user_session UUID NOT NULL"
    sql1 +=      ");"

    sql2 = f"CREATE TEMP TABLE staging_{tablename} (LIKE {tablename} "
    sql2 += "INCLUDING DEFAULTS EXCLUDING CONSTRAINTS) ON COMMIT DROP;"

    sql3 = f"ALTER TABLE staging_{tablename} ALTER COLUMN user_session DROP NOT NULL;"

    sql4 = f"COPY staging_{tablename} FROM STDIN "
    sql4 += "WITH (FORMAT csv, HEADER true, DELIMITER ',');"

    sql5 = f"INSERT INTO {tablename} SELECT * FROM staging_{tablename} " 
    sql5 += "WHERE user_session IS NOT NULL AND user_id IS NOT NULL "
    sql5 += "  AND price IS NOT NULL AND product_id IS NOT NULL "
    sql5 += "  AND event_type IS NOT NULL AND event_time IS NOT NULL ;"    

    with psycopg.connect(
        "host=127.0.0.1 port=5432 dbname=piscineds user=luicasad password=mysecretpasswd"
    ) as conn:
        with conn.cursor() as cur:
            # cur.execute("SELECT version();")
            cur.execute(sql0)
            exists = cur.fetchone()[0]
            if exists:
                print(f"Table {tablename} exists. Nothing done")
                cur.close()
                conn.close()
            else:
                cur.execute(sql1)
                print(f"Table {tablename} created succesfully")
                try:
                    cur.execute(sql2)
                    cur.execute(sql3)
                    print(f"Temporal table staging_{tablename} created succesfully")
                    with open(table_path, "r", encoding="utf-8") as f:
                        with cur.copy(sql4) as copy:
                            copy.write(f.read())
                    cur.execute(f"SELECT COUNT(*) FROM staging_{tablename};")
                    rows_staged = cur.fetchone()[0];
                    print(f"Temp Table populated succesfully with {rows_staged} rows.")
                    cur.execute(sql5)
                    conn.commit()        
                    cur.execute(f"SELECT COUNT(*) FROM {tablename};")
                    rows_imported = cur.fetchone()[0];
                    print(f"Table {tablename} populated succesfully with {rows_imported} rows")
                    print(f"{rows_staged - rows_imported} having some feature with NULL values were dropped ")
                except Exception as e:
                    conn.rollback()
                    print(f"Error importing {table_path}: {e}")
                finally:
                    cur.close()
                    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python ./table.py <table's path>")
        sys.exit(1)
    main(path_test(sys.argv[1]))

