from loguru import logger

from ..base import BaseFeature


class Sport(BaseFeature):
    name = "sport"

    def check(self):
        pass

    def run(self):
        logger.info(f"{self.name} running")
