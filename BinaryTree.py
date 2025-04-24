from typing import List, Set, Tuple
from utils import *


# класс для описания дерева
class BinaryTree:
    # @timer
    def __init__(self, edges: List[Tuple[int, int]], size: int):
        self.size = size
        self.graph = [[] for _ in range(self.size)]

        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

    # поиск в глубину для обхода дерева
    def dfs(self, v : int, visited : Set[int], exclude : Set[int]):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited and neighbor not in exclude:
                self.dfs(neighbor, visited, exclude)

    # поиск поддеревьев без исключенных вершин
    @timer
    def find_subtree(self, exclude: Set[int]) -> List[List[int]]:
        subtrees = []
        global_visited = set()

        for node in range(self.size):
            # если вершина не посещена и не исключена, начинаем обход - поддерево - с неё
            if node not in global_visited and node not in exclude:
                subtree = set()
                self.dfs(node, subtree, exclude)
                subtrees.append(list(subtree))
                global_visited.update(subtree)

        return subtrees