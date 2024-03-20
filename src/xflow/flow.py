import typing as t

from xflow.base import BaseStage
from xflow.exceptions import XFlowException
from xflow.graph import StageGraph
from xflow.stages import STAGES


class Flow:
    def __init__(self, entry: t.Type[BaseStage]) -> None:
        self.entry = entry
        self.stage_names = []

    def run(self):
        print(f"Flow start run by entry Stage[{self.entry.name}]")
        self.init()
        self.check()
        self.start()

    def start(self):
        if not self.entry:
            raise XFlowException(f"Not found stage link by Stage[{self.entry.name}]")

        for stage_name in self.stage_names:
            STAGES[stage_name].run()

    def check(self):
        self.check_stage_completed()

    def check_stage_completed(self):
        """Check link stage completed"""
        for stage_name in self.stage_names:
            if stage_name == self.entry.name:
                break
            if not STAGES[stage_name].completed():
                raise XFlowException(f"Stage[{stage_name} not completed]")

    def init(self):
        self.init_stage_names()

    def init_stage_names(self):
        self.stage_names = StageGraph.get_node_chain(self.entry.name)
