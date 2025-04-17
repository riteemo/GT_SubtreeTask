from typing import List, Tuple


# класс для конвертации дерева в матрицу смежности и наоборот
class MatrixConverter:
    # конвертация списка рёбер в матрицу смежности
    def tree_to_matrix(self, edges : List[Tuple[int, int]], size : int) -> List[List[int]]:
        matrix : List[List[int]] = [[0] * size for _ in range(size)]

        for u, v in edges:
            matrix[u][v] = 1
            matrix[v][u] = 1
        return matrix

    # конвертация матрицы смежности в список рёбер
    def matrix_to_tree(self, matrix : List[List[int]]) -> List[Tuple[int, int]]:
        size : int = len(matrix)
        edges : List[Tuple[int, int]] = []

        for i in range(size):
            for j in range(i+1, size):
                if matrix[i][j] == 1:
                    edges.append((i, j))
        return edges