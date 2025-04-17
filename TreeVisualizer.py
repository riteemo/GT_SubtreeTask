from typing import List, Set

# класс для визуализации
class TreeVisualizer:
    def print_tree(self, graph : List[List[int]], nodes : List[int], root: int, visited: Set[int] = None,
                   prefix : str = "", is_last : bool = True):
        if visited is None:
            visited = set()
        visited.add(root)

        # вывод текущей вершины
        connector = "└── " if is_last else "├── "
        print(prefix + connector + str(root))

        new_prefix = prefix + ("    " if is_last else "│   ")

        # поиск потомков
        children = sorted([node for node in graph[root] if node in nodes and node not in visited])

        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            self.print_tree(graph, nodes, child, visited, new_prefix, is_last_child)

    def visualize(self, graph : List[List[int]], subtrees : List[List[int]] = None):
        if subtrees:
            for index, subtree in enumerate(subtrees):
                print(f"Subtree {index + 1}:")
                self.print_tree(graph, subtree, min(subtree))
        else:
            print("Full tree:")
            self.print_tree(graph, list(range(len(graph))), 0)