from loguru import logger
from xflow.base import BaseFeature


class Eat(BaseFeature):
    name = "eat"

    def check(self):
        pass

    def run(self):
        logger.info(f"{self.name} running")
