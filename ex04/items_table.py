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
    tablename = os.path.splitext(basename)[0]+"s"  # subject dixit.
    sql0 = psycopg.sql.SQL("""
        SELECT EXISTS (SELECT 1 FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_name = {});
    """).format(psycopg.sql.Literal(tablename))

    sql1 = psycopg.sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            category_id   BIGINT,        
            product_id    INTEGER NOT NULL,
            category_code TEXT,
            brand         TEXT
        );
    """).format(psycopg.sql.Identifier(tablename))


    csv_columns = ["product_id", "category_id", "category_code", "brand"]

    sql4 = psycopg.sql.SQL("""
        COPY {} ({}) FROM STDIN
        WITH (FORMAT csv, HEADER MATCH, DELIMITER ',');
    """).format(
        psycopg.sql.Identifier(tablename),
        psycopg.sql.SQL(", ").join(map(psycopg.sql.Identifier, csv_columns)),
    )



    with psycopg.connect(
        host="127.0.0.1", port=5432, dbname="piscineds", user="luicasad"
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
                    with open(table_path, "r", encoding="utf-8") as f:
                        with cur.copy(sql4) as copy:
                            copy.write(f.read())
                    cur.execute(f"SELECT COUNT(*) FROM {tablename};")
                    rows_imported = cur.fetchone()[0];
                    conn.commit()        
                    print(f"Table {tablename} populated succesfully with {rows_imported} rows")
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

