import abc
import typing as t


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
        for feature in self.features:
            feature.check()
            feature.run()
