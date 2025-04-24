from TreeGenerator import TreeGenerator
from FileManager import FileManager
from BinaryTree import BinaryTree
from TreeVisualizer import TreeVisualizer


def main():
    generator = TreeGenerator() # объект генерации дерева
    file_manager = FileManager() # объект для работы с файлами
    visualizer = TreeVisualizer() # объект для визуализации

    filename = "tree.txt"
    edges = None # переменная для хранения ребер
    tree = None
    n = 0 # количество вершин в дереве

    while True:
        print("\nMenu:")
        print("1 — Generate the tree") # генерация дерева
        print("2 — Load tree from file") # загрузка из файла
        print("3 — Show the tree") # визуализация дерева
        print("4 — Find subtrees without input vertices") # найти поддеревья, исключив заданные вершины
        print("5 — Save tree to file") # сохранение в файл
        print("0 — Exit")

        try:
            choice = input("Choose: ")

            if choice == "1":
                try:
                    n = int(input("Input number of vertices: "))
                    if n <= 0:
                        raise ValueError("The number of vertices must be positive")
                    edges = generator.generate_tree(n)
                    tree = BinaryTree(edges, n)
                    print("Tree is generated.")
                except ValueError as e:
                    print(f"Invalid value: {e}")

            elif choice == "2":
                try:
                    filename = input("Enter the filename + .txt: ")
                    edges = file_manager.read_graph(filename)
                    n = len(edges) + 1
                    tree = BinaryTree(edges, n)
                    print(f"The tree is loaded from {filename}")
                except FileNotFoundError:
                    print("File not found")
                except Exception as e:
                    print(f"Error loading: {e}")


            elif choice == "3":
                if tree:
                    print("Full tree: ")
                    visualizer.print_tree(tree.graph, list(range(n)), 0)
                else:
                    print("Firstly load or generate the tree")

            elif choice == "4":
                if tree:
                    try:
                        exclude_input = input("Enter the numbers of the vertices to exclude separated by a space: ")
                        exclude = set(map(int, exclude_input.strip().split())) if exclude_input else set()

                        subtrees = tree.find_subtree(exclude)
                        if not subtrees:
                            print("No subtrees were found without the specified vertices")
                        else:
                            print("\nFounded subtrees:")
                            visualizer.visualize(tree.graph, subtrees)
                    except ValueError:
                        print("Invalid input")
                else:
                    print("Firstly load or generate the tree")

            elif choice == "5":
                if edges is not None:
                    try:
                        filename = input("Enter the filename + .txt: ")
                        file_manager.save_graph(edges, filename)
                        print(f"The tree is saved to {filename}")
                    except Exception as e:
                        print(f"Error saving: {e}")
                else:
                    print("Firstly load or generate the tree")

            elif choice == "0":
                print("Bye!")
                break

            else:
                print("Invalid input")

        except Exception as e:
            print(f"You've ruined everything. So what did you get in return? \nError text: {e}")

if __name__ == "__main__":
    main()