from pathlib import Path

from loguru import logger
from yaml import load

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
