import os
from pathlib import Path
import json

import fsos

DEFAULT_ROOT_PATH = str(Path(Path.home(), ".fsos"))
DEFAULT_FSOS_NAME = ".fsos"


def _get_version() -> dict:
    return {
        "fsos_version": fsos.__version__
    }


def _init_db(db: dict) -> None:
    fsos._FSOS_DB = db


def _get_db() -> dict:
    return fsos._FSOS_DB


def _check_fsos(ROOT_PATH=DEFAULT_ROOT_PATH):
    return Path(os.path.join(ROOT_PATH), DEFAULT_FSOS_NAME).exists()


def _create_fsos(ROOT_PATH=DEFAULT_ROOT_PATH):
    Path(DEFAULT_ROOT_PATH).mkdir(parents=True, exist_ok=True)
    _init_db({**_get_version(), **{"buckets": {}}})
    _update_fsos(ROOT_PATH)


def _update_fsos(ROOT_PATH=DEFAULT_ROOT_PATH):
    with open(Path(os.path.join(ROOT_PATH), DEFAULT_FSOS_NAME), 'w') as out:
        json.dump(_get_db(), out)


def _load_fsos(ROOT_PATH=DEFAULT_ROOT_PATH):
    with open(Path(os.path.join(ROOT_PATH), DEFAULT_FSOS_NAME), 'r') as out:
        temp_db = None
        json.load(out, temp_db)
        _init_db(temp_db)


def _add_bucket(bucket_name: str, ROOT_PATH=DEFAULT_ROOT_PATH):
    return


def _remove_bucket(bucket_name: str, ROOT_PATH=DEFAULT_ROOT_PATH):
    return


def _add_object(bucket_name: str, object_name: str, object: bytes, ROOT_PATH=DEFAULT_ROOT_PATH, ignore_exist=False):
    pass


def _remove_object(bucket_name: str, object_name: str, ROOT_PATH=DEFAULT_ROOT_PATH):
    pass


def _update_object(bucket_name, object_name: str, object: bytes, ROOT_PATH=DEFAULT_ROOT_PATH):
    pass
