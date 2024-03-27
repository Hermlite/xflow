from pathlib import Path

from loguru import logger
from yaml import load

from .exceptions import XFlowConfigException
from .graph import StageGraph
from .stages import STAGES

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    workpath: Path

    @classmethod
    def from_yaml(cls, yaml_path):
        with open(yaml_path, "r") as fd:
            data = load(fd, Loader=Loader)
        logger.info("Config data is {}", data)
        cls.workpath = Path(data.get("workpath"))

        graph = data.get("graph")
        if not graph:
            raise XFlowConfigException("Undefine graph")
        for stage_name in graph:
            if stage_name not in STAGES:
                raise XFlowConfigException(f"Unknown Stage[{stage_name}]")
            for ede_stage_name in graph[stage_name]:
                if ede_stage_name not in STAGES:
                    raise XFlowConfigException(f"Unknown Stage[{stage_name}]")
                StageGraph.add_edge(stage_name, ede_stage_name)
