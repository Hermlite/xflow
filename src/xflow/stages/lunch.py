from ..base import BaseStage
from ..features.cook import Cook
from ..features.eat import Eat
from ..stages import register


@register
class Lunch(BaseStage):
    name = "lunch"
    features = [Cook(), Eat()]
