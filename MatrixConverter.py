from typing import List, Tuple


# класс для конвертации дерева в матрицу смежности
class MatrixConverter:
    # конвертация списка рёбер в матрицу смежности
    def tree_to_matrix(self, edges : List[Tuple[int, int]], size : int) -> List[List[int]]:
        matrix : List[List[int]] = [[0] * size for _ in range(size)]

        for u, v in edges:
            matrix[u][v] = 1
            matrix[v][u] = 1
        return matrix