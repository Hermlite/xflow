from xflow.base import BaseStage
from xflow.features.sport import Sport
from xflow.stages import register


@register
class Dinner(BaseStage):
    name = "dinner"
    features = [Sport()]

    def completed(self):
        return True
