from os.path import normpath, join

from fsos import fs_manager as fsm
from fsos.deco import os_failure_checker

"""
OS structure
{
    FSOS_BUCKET_KEY : {
        "Bucket_key" : {
            "Object_key" : {
                "path" : relative_file_path
                "meta" : meta_info
            }
        }
    },
    FSOS_VERSION_KEY : {
        version
    }
}
"""


@os_failure_checker
def _list_bucket(ROOT_PATH: str) -> list:
    """get list of bucket in root fsos"""
    return list(fsm._get_db()[fsm.FSOS_BUCKET_KEY].keys())


@os_failure_checker
def _check_bucket(bucket_name: str, ROOT_PATH: str) -> bool:
    """check bucket is exist in root fsos"""
    return bucket_name in fsm._get_db()[fsm.FSOS_BUCKET_KEY].keys()


@os_failure_checker
def _add_bucket(bucket_name: str, ROOT_PATH: str) -> bool:
    """add bucket folder & fsos db"""
    fsm._get_db()[fsm.FSOS_BUCKET_KEY][bucket_name] = {}
    fsm._create_folder(ROOT_PATH, bucket_name)
    return True


@os_failure_checker
def _remove_bucket(bucket_name: str, ROOT_PATH: str) -> bool:
    """remove bucket folder & fsos db"""
    del fsm._get_db()[fsm.FSOS_BUCKET_KEY][bucket_name]
    fsm._remove_folder(ROOT_PATH, bucket_name)
    return True


@os_failure_checker
def _copy_object(
    bucket_name: str,
    object_name: str,
    from_path: str,
    ROOT_PATH: str,
    ignore_exist=False,
) -> bool:
    """copy file in fsos system"""
    fsm._get_db()[fsm.FSOS_BUCKET_KEY][bucket_name][object_name] = {
        "path": f"{bucket_name}/{object_name}",
        "meta": {},
    }
    fsm._copy_file(
        normpath(from_path), normpath(join(ROOT_PATH, bucket_name, object_name))
    )
    return True


@os_failure_checker
def _add_object(
    bucket_name: str,
    object_name: str,
    object: bytes,
    ROOT_PATH: str,
    ignore_exist=False,
) -> bool:
    """save byte in fsos system"""
    # TODO
    return True


@os_failure_checker
def _remove_object(bucket_name: str, object_name: str, ROOT_PATH: str) -> bool:
    del fsm._get_db()[fsm.FSOS_BUCKET_KEY][bucket_name][object_name]
    fsm._remove_file(normpath(join(ROOT_PATH, bucket_name, object_name)))
    return True


@os_failure_checker
def _update_object_meta(
    bucket_name: str, object_name: str, meta_info: dict, ROOT_PATH: str
) -> bool:
    object_info = fsm._get_db()[fsm.FSOS_BUCKET_KEY][bucket_name][object_name]
    object_info["meta"] = meta_info
    return True


def _update_object(
    bucket_name: str, object_name: str, object: bytes, ROOT_PATH: str
) -> bool:
    # TODO
    return True


@os_failure_checker
def _list_object(bucket_name: str, ROOT_PATH: str) -> list:
    return list(fsm._get_db()[fsm.FSOS_BUCKET_KEY][bucket_name].keys())
