from ..base import BaseStage
from ..features.sport import Sport
from ..stages import register


@register
class Dinner(BaseStage):
    name = "dinner"
    features = [Sport()]
