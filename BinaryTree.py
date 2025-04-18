from typing import List, Set
from utils import *

# класс для описания дерева
class BinaryTree:
    def __init__(self, matrix : List[List[int]]):
        self.size = len(matrix)
        self.graph = [[] for _ in range(self.size)]

        # создание списка списков, где для каждой вершины будут храниться все соседи
        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j] == 1:
                    self.graph[i].append(j)

    # поиск в глубину для обхода дерева
    def dfs(self, v : int, visited : Set[int], exclude : Set[int]):
        try:
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited and neighbor not in exclude:
                    self.dfs(neighbor, visited, exclude)
        except Exception as e:
            print(f"Error with dfs: {e}")

    # поиск поддеревьев без исключенных вершин
    @timer
    def find_subtree(self, exclude: Set[int]) -> List[List[int]]:
        try:
            subtrees = []
            global_visited = set()

            invalid_nodes = [node for node in exclude if node < 0 or node >= self.size]
            if invalid_nodes:
                raise Exception(f"There are non-existent vertices")
            else:
                for node in range(self.size):
                    # если вершина не посещена и не исключена, начинаем обход - поддерево - с неё
                    if node not in global_visited and node not in exclude:
                        subtree = set()
                        self.dfs(node, subtree, exclude)
                        subtrees.append(list(subtree))
                        global_visited.update(subtree)

                return subtrees
        except Exception as e:
            print(f"Error with subtrees  : {e}")
