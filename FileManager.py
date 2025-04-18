from typing import List


# класс для работы с файлом
class FileManager:
    # сохранение матрицы в файл
    def save_matrix(self, matrix : List[List[int]], filename : str) -> None:
        try:
            with open(filename, 'w') as file:
                for row in matrix:
                    file.write(' '.join(map(str, row)) + '\n')
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error saving: {e}")

    # чтение матрицы из файла
    def read_matrix(self, filename : str) -> List[List[int]]:
        try:
            with open(filename, 'r') as file:
                return [list(map(int, line.strip().split())) for line in file]
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error loading: {e}")