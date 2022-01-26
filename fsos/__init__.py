import sys
from pathlib import Path

this = sys.modules[__name__]
this._FSOS_DB = None

__all__ = ["fsos"]
__version__ = "0.0.1"

DEFAULT_ROOT_PATH = str(Path(Path.home(), ".fsos"))
DEFAULT_FSOS_NAME = ".fsos"
