from fsos import fs_manager as fs
from fsos.deco import fsos_init_checker


@fsos_init_checker
def make_bucket(bucket_name: str, root_path: str) -> bool:
    return


@fsos_init_checker
def remove_bucket(bucket_name: str, root_path: str) -> bool:
    return


@fsos_init_checker
def bucket_exists(bucket_name: str, root_path: str) -> bool:
    return


@fsos_init_checker
def list_buckets(bucket_name: str, root_path: str) -> bool:
    return


@fsos_init_checker
def list_objects(bucket_name: str, root_path: str):
    return


@fsos_init_checker
def put_filepath(bucket_name: str, object_name: str, root_path: str):
    return


@fsos_init_checker
def get_filepath(bucket_name: str, object_name: str, root_path: str):
    return


# def put_objects(bucket_name: str, object_name: str, root_path: str):
#     return


# def get_objects(bucket_name: str, object_name: str, root_path: str):
#     return
