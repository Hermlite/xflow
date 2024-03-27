import argparse
import sys
from pathlib import Path

from loguru import logger

from .config import Config
from .flow import Flow
from .stages import STAGES

logger.remove()
logger.add(sys.stderr, level="DEBUG")


def cli():
    logger.info("All stages are {}", STAGES)
    parser = argparse.ArgumentParser(description="XFlow")
    parser.add_argument("--config", "-c", help="Config File", required=True, type=Path)
    parser.add_argument(
        "--stage", "-s", help="Stage Name", required=True, choices=STAGES.keys()
    )
    args = parser.parse_args()

    Config.from_yaml(args.config)

    Flow(Config.workpath, STAGES[args.stage]).run()
