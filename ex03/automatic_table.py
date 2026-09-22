import sys
import os
import re
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ex02.table import main  # noqa: E402
from ex02.table import path_test  # noqa: E402

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: automatic_table <path to folder>")
        sys.exit(1)


    carpeta = Path(sys.argv[1])

    meses = "jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec"
    patron = re.compile(rf"data_202[23]_({meses})\.csv", re.IGNORECASE)

    ficheros = sorted(
        f for f in carpeta.iterdir()
        if f.is_file() and patron.fullmatch(f.name)
    )

    for f in ficheros:
        main(path_test(f))