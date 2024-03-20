from xflow.base import BaseStage
from xflow.features.cook import Cook
from xflow.features.eat import Eat
from xflow.stages import register


@register
class Lunch(BaseStage):
    name = "lunch"
    features = [Cook(), Eat()]

    def completed(self):
        return False
