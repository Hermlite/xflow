from xflow.base import BaseStage
from xflow.features.cook import Cook
from xflow.features.eat import Eat
from xflow.features.sport import Sport
from xflow.stages import register


@register
class Breakfast(BaseStage):
    name = "breakfast"
    features = [Cook(), Eat(), Sport()]

    def completed(self):
        return True
