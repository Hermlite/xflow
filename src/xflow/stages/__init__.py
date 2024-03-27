import importlib
import pathlib
import typing as t

from loguru import logger

if t.TYPE_CHECKING:
    from ..base import BaseStage


STAGES: t.Dict[str, "BaseStage"] = {}


def register(cls):
    logger.debug(f"register {cls} to {cls.name}")
    STAGES[cls.name] = cls()
    return cls


for f in pathlib.Path(__file__).parent.glob("*.py"):
    if f.name == "__init__.py":
        continue
    importlib.import_module(f".{f.stem}", package="xflow.stages")
