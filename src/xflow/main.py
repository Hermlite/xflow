import pathlib
import sys

from loguru import logger

from .flow import Flow
from .graph import StageGraph
from .stages.breakfast import Breakfast
from .stages.dinner import Dinner
from .stages.lunch import Lunch

logger.remove()
logger.add(sys.stderr, level="DEBUG")

StageGraph.add_edge(Breakfast.name, Lunch.name)
StageGraph.add_edge(Breakfast.name, Dinner.name)
logger.debug(f"Graph is {StageGraph.GRAPH}")


def cli():
    workpath = pathlib.Path("./xflow-workpath-demo")
    workpath.mkdir(exist_ok=True)
    f1 = Flow(workpath, Dinner)
    f1.run()

    f2 = Flow(workpath, Lunch)
    f2.run()
