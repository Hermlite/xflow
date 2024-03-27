import argparse
import sys
from pathlib import Path

from loguru import logger

from .config import Config
from .flow import Flow
from .graph import StageGraph
from .stages import STAGES
from .stages.breakfast import Breakfast
from .stages.dinner import Dinner
from .stages.lunch import Lunch

logger.remove()
logger.add(sys.stderr, level="DEBUG")


def demo():
    StageGraph.add_edge(Breakfast.name, Lunch.name)
    StageGraph.add_edge(Breakfast.name, Dinner.name)
    logger.debug(f"Graph is {StageGraph.GRAPH}")


def cli():
    logger.info("All stages are {}", STAGES)
    parser = argparse.ArgumentParser(description="XFlow")
    parser.add_argument("--config", "-c", help="Config File", required=True, type=Path)
    parser.add_argument(
        "--stage", "-s", help="Stage Name", required=True, choices=STAGES.keys()
    )
    args = parser.parse_args()

    Config.from_yaml(args.config)

    demo()

    Flow(Config.workpath, STAGES[args.stage]).run()
