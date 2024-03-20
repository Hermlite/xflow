from xflow.flow import Flow
from xflow.graph import StageGraph
from xflow.stages.breakfast import Breakfast
from xflow.stages.dinner import Dinner
from xflow.stages.lunch import Lunch

StageGraph.add_edge(Breakfast.name, Lunch.name)
StageGraph.add_edge(Breakfast.name, Dinner.name)
print(f"Graph is {StageGraph.GRAPH}")


def cli():
    f1 = Flow(Dinner)
    f1.run()

    f2 = Flow(Lunch)
    f2.run()
