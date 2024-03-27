import abc
import typing as t

from loguru import logger


class BaseFeature(abc.ABC):
    name: str

    @abc.abstractmethod
    def check(self):
        """If current feature can run"""

    @abc.abstractmethod
    def run(self):
        """Feature main"""


class BaseStage(abc.ABC):
    name: str
    features: t.List[BaseFeature]
    depend: t.Optional["BaseStage"] = None

    def run(self):
        logger.debug(f"Stage[{self.name}] depend on stage[{self.depend}]")
        for feature in self.features:
            feature.check()
            feature.run()

    def __str__(self) -> str:
        return rf"Stage[{self.name}]"
