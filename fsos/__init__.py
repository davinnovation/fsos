import sys
import fsos.bucket_manager as bm

this = sys.modules[__name__]
this._FSOS_DB = None

__all__ = ['fsos']
__version__ = '0.0.1'
