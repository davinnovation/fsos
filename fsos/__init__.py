import sys
import fsos.bucket_manager as bm
import fsos.fs_manager as fs

this = sys.modules[__name__]
this._FSOS_DB = None

__all__ = ['fsos']
__version__ = '0.0.1'
