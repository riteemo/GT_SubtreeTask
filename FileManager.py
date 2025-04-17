from typing import List


# класс для работы с файлом
class FileManager:
    # сохранение матрицы в файл
    def save_matrix(self, matrix : List[List[int]], filename : str) -> None:
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(' '.join(map(str, row)) + '\n')

    # чтение матрицы из файла
    def read_matrix(self, filename : str) -> List[List[int]]:
        with open(filename, 'r') as file:
            return [list(map(int, line.strip().split())) for line in file]