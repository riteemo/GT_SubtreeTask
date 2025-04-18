from typing import List, Tuple


# класс для конвертации дерева в матрицу смежности
class MatrixConverter:
    # проверка на матрицу
    def is_matrix(self, matrix : List[List[int]]) -> bool:
        size = len(matrix)
        # проверка совпадения количества строк - столбцов
        if not all(len(row) == size for row in matrix):
            return False
        # проверка элементов внутри матрицы
        if not all(all(isinstance(elem, int) for elem in row) for row in matrix):
            return False
        return True
    # конвертация списка рёбер в матрицу смежности
    def tree_to_matrix(self, edges : List[Tuple[int, int]], size : int) -> List[List[int]]:
        try:
            matrix : List[List[int]] = [[0] * size for _ in range(size)]

            for u, v in edges:
                matrix[u][v] = 1
                matrix[v][u] = 1
            return matrix
        except Exception as e:
            print(f"Nothing to convert: {e}")
