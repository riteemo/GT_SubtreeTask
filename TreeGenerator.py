import random
from typing import List, Tuple

# класс для генерации деревьев
class TreeGenerator:
    def generate_tree(self, size : int) -> List[Tuple[int, int]]:
        edges : List[Tuple[int, int]] = [] # массив с кортежами (ребрами)
        children_counter = {0:0} # словарь для подсчета количества потомков

        for i in range(1, size):
            # возможные родители, у которых потомков меньше двух
            possible_parents = [node for node, count in children_counter.items() if count < 2]

            parent = random.choice(possible_parents)
            edges.append((parent, i))

            # обновление количества потомков
            children_counter[parent] += 1
            children_counter[i] = 0 # у новой вершины будет 0 потомков

        return edges