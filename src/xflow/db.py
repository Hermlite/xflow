import typing as t
from pathlib import Path

from tinydb import TinyDB

from .exceptions import XFlowDBException


class DB:
    def __init__(self, root_path: Path, stage_names: t.List[str]) -> None:
        self.root_path = root_path
        self.stage_names = stage_names
        self._db: t.Dict[str, TinyDB] = {}
        self.init()

    def init(self):
        self.root_path.mkdir(exist_ok=True)
        for stage_name in self.stage_names:
            db_path = self.root_path / f"{stage_name}.json"
            if not db_path.exists():
                raise XFlowDBException(f"Stage[{stage_name}] DB not exists")
            self._db[stage_name] = TinyDB(db_path)
