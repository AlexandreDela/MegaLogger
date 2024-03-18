"""
__init__ of the module megalogger
"""

__version__ = "0.0.1"

from .abstract_logger import AbstractLogger, AbstractDelayed, AbstractInstant
from .megalogged import (
    MegaLoggedItemTuple,
    MegaLoggedItemString,
    MegaLoggedItem,
)
from .blueprints import (
    DelayedStreamLoggerBlueprint,
    InstantStreamLoggerBlueprint,
    PandasODSLoggerBlueprint,
    PandasExcelLoggerBlueprint,
    PandasSQLLoggerBlueprint,
)
