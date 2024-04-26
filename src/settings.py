import pathlib

SRC_PATH = pathlib.Path(__file__).absolute().parent
PROJECT_PATH = pathlib.Path(SRC_PATH).absolute().parent

SQLITE_PATH = pathlib.Path(SRC_PATH, "database", "database.db")
SQLITE_ACCESS = f"sqlite+aiosqlite:///{SQLITE_PATH}"
