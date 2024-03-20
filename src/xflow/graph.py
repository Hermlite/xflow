import typing as t
from collections import defaultdict


class StageGraph:
    GRAPH: t.Dict[str, t.List[str]] = defaultdict(list)

    @classmethod
    def add_edge(cls, node, child):
        cls.GRAPH[node].append(child)

    @classmethod
    def get_node_chain(cls, node) -> t.List[str]:
        chain = []

        def dfs(current_node, current_chain):
            current_chain.append(current_node)
            if current_node == node:
                chain.extend(current_chain)
            for child in cls.GRAPH[current_node]:
                dfs(child, current_chain)

            current_chain.pop()

        dfs(next(iter(cls.GRAPH.keys())), [])
        return chain
