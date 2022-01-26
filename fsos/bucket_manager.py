from pathlib import Path

from fsos import DEFAULT_ROOT_PATH
from fsos import fs_manager as fsm
from fsos import os_manager as osm
from fsos.deco import fsos_init_checker


@fsos_init_checker
def make_bucket(bucket_name: str, root_path: str = DEFAULT_ROOT_PATH) -> bool:
    return (
        False
        if not osm._check_bucket(bucket_name, root_path)
        else osm._add_bucket(bucket_name, root_path)
    )


@fsos_init_checker
def remove_bucket(bucket_name: str, root_path: str = DEFAULT_ROOT_PATH) -> bool:
    return (
        False
        if not osm._check_bucket(bucket_name, root_path)
        else osm._remove_bucket(bucket_name, root_path)
    )


@fsos_init_checker
def bucket_exists(bucket_name: str, root_path: str = DEFAULT_ROOT_PATH) -> bool:
    return osm._check_bucket(bucket_name, root_path)


@fsos_init_checker
def list_buckets(root_path: str = DEFAULT_ROOT_PATH) -> bool:
    return osm._list_bucket(root_path)


@fsos_init_checker
def list_objects(bucket_name: str, root_path: str = DEFAULT_ROOT_PATH):
    return osm._list_object(bucket_name, root_path)


@fsos_init_checker
def put_filepath(
    bucket_name: str,
    object_name: str,
    from_filepath: str,
    root_path: str = DEFAULT_ROOT_PATH,
) -> bool:
    osm._copy_object(bucket_name, object_name, from_filepath, root_path)
    return True


@fsos_init_checker
def get_filepath(
    bucket_name: str, object_name: str, root_path: str = DEFAULT_ROOT_PATH
) -> list:
    temp_list = []
    for object_key in osm._list_object(bucket_name, root_path):
        temp_list.append(
            Path(root_path, fsm._get_db()[bucket_name][object_key]["path"])
        )
    return temp_list


# def put_objects(bucket_name: str, object_name: str, root_path: str):
#     return


# def get_objects(bucket_name: str, object_name: str, root_path: str):
#     return
