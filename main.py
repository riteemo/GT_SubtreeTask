from TreeGenerator import TreeGenerator
from MatrixConverter import MatrixConverter
from FileManager import FileManager
from BinaryTree import BinaryTree
from TreeVisualizer import TreeVisualizer


def main():
    generator = TreeGenerator()
    converter = MatrixConverter()
    file_manager = FileManager()
    visualizer = TreeVisualizer()

    filename = "tree.txt"
    matrix = None
    tree = None
    n = 0

    while True:
        print("\nMenu:")
        print("1 — Generate the tree")
        print("2 — Load tree from file")
        print("3 — Show the tree")
        print("4 — Find subtrees without input vertices")
        print("5 — Save tree to file")
        print("0 — Exit")

        try:
            choice = input("Choose: ")

            if choice == "1":
                try:
                    n = int(input("Input number of vertices: "))
                    if n <= 0:
                        raise ValueError("The number of vertices must be positive")
                    edges = generator.generate_tree(n)
                    matrix = converter.tree_to_matrix(edges, n)
                    tree = BinaryTree(matrix)
                    print("Tree is generated.")
                except ValueError as e:
                    print(f"Invalid value: {e}")

            elif choice == "2":
                try:
                    filename = input("Enter the filename + .txt: ")
                    matrix = file_manager.read_matrix(filename)
                    n = len(matrix)
                    tree = BinaryTree(matrix)
                    print(f"The tree is loaded from {filename}")
                except FileNotFoundError:
                    print("File not found")
                except Exception as e:
                    print(f"Error loading: {e}")


            elif choice == "3":
                if tree:
                    visualizer.print_tree(tree.graph, list(range(n)), 0)
                else:
                    print("Firstly load or generate the tree")

            elif choice == "4":
                if tree:
                    try:
                        exclude_input = input("Enter the numbers of the vertices to exclude separated by a space: ")
                        exclude = set(map(int, exclude_input.strip().split())) if exclude_input else set()

                        invalid_nodes = [node for node in exclude if node < 0 or node >= n]
                        if invalid_nodes:
                            print(f"Error: there are non-existent vertices")
                        else:
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
                if matrix is not None:
                    try:
                        filename = input("Enter the filename + .txt: ")
                        file_manager.save_matrix(matrix, filename)
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