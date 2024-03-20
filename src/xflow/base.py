import abc
import typing as t

from xflow.exceptions import XFlowFeatureError


class BaseFeature(abc.ABC):
    name: str

    @abc.abstractmethod
    def check(self) -> bool:
        """If current feature can run"""

    @abc.abstractmethod
    def run(self):
        pass


class BaseStage(abc.ABC):
    name: str
    features: t.List[BaseFeature]

    @abc.abstractmethod
    def completed(self) -> bool:
        """If current stage has completed"""

    def run(self):
        for feature in self.features:
            if not feature.check():
                raise XFlowFeatureError(f"Feature[{feature.name}] check fail")
            feature.run()
