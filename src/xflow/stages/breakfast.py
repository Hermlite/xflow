from ..base import BaseStage
from ..features.cook import Cook
from ..features.eat import Eat
from ..features.sport import Sport
from ..stages import register


@register
class Breakfast(BaseStage):
    name = "breakfast"
    features = [Cook(), Eat(), Sport()]

    def completed(self):
        pass
