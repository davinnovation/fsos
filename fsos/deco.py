from inspect import getfullargspec
from functools import wraps

from fsos import fs_manager as fs

BUCKET_ARGNAME = 'bucket_name'


def fsos_init_checker(func):
    argspec = getfullargspec(func)
    argument_index = argspec.args.index(BUCKET_ARGNAME)
    @wraps(func)
    def pre_check(*args, **kwargs):
        try:
            value = args[argument_index]
        except IndexError:
            value = kwargs[BUCKET_ARGNAME]
        if not fs._check_fsos(value):
            fs._create_fsos()
        return func(*args, **kwargs)
    return pre_check
