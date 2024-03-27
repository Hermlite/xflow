import typing as t
from pathlib import Path

from loguru import logger

from .base import BaseStage
from .db import DB
from .exceptions import XFlowException
from .graph import StageGraph
from .stages import STAGES


class Flow:
    def __init__(self, workpath: Path, entry: t.Type[BaseStage]) -> None:
        self.workpath = workpath
        self.entry = entry
        self.stage_names = []
        self.db: DB = None

    def run(self):
        self.stage_names = StageGraph.get_node_chain(self.entry.name)
        if not self.stage_names:
            raise XFlowException(f"Not found stage link by Stage[{self.entry.name}]")

        db_path = self.workpath / "db"
        db_path.mkdir(exist_ok=True)
        self.db = DB(db_path, self.stage_names)

        depend = None
        for stage_name in self.stage_names:
            if stage_name not in STAGES:
                raise XFlowException(f"Stage[{stage_name}] not exists")

            current_stage = STAGES[stage_name]
            if depend:
                current_stage.depend = depend
            else:
                depend = current_stage

            if stage_name == self.entry.name:
                logger.info(f"XFlow running by entry Stage[{self.entry.name}]")
                self.entry().run()
                break
