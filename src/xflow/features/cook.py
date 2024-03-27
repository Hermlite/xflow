from loguru import logger
from xflow.base import BaseFeature


class Cook(BaseFeature):
    name = "cook"

    def check(self):
        pass

    def run(self):
        logger.info(f"{self.name} running")
