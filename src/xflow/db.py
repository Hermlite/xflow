import typing as t
from pathlib import Path

from tinydb import TinyDB

from .exceptions import XFlowDBException


class DB:
    collections: t.Dict[str, TinyDB] = {}

    @classmethod
    def init(cls, root_path: Path, stage_names: t.List[str]):
        root_path.mkdir(exist_ok=True)

        if len(stage_names) == 1:
            return

        for stage_name in stage_names:
            db_path = root_path / f"{stage_name}.json"
            if not db_path.exists():
                raise XFlowDBException(f"Stage[{stage_name}] DB not exists")
            cls.collections[stage_name] = TinyDB(db_path)
