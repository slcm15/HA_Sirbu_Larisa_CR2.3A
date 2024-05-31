from dfs import depth_first_search, TimeoutException
from ucs import uniform_cost_search
from astar import a_star_search
import numpy as np


def load_tsp_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    extracting = False
    matrix = []

    for line in data.split('\n'):
        line = line.strip()
        if 'EDGE_WEIGHT_SECTION' in line:
            extracting = True
            continue
        if 'DISPLAY_DATA_SECTION' in line or 'EOF' in line:
            break
        if extracting and line:
            row = list(map(int, line.split()))
            matrix.append(row)

    return np.array(matrix)


def main():
    file_path = 'bays29.tsp'
    distance_matrix = load_tsp_data(file_path)

    print("Matricea de distanțe:")
    print(distance_matrix)

    # Apel DFS
    try:
        path_dfs, cost_dfs = depth_first_search(distance_matrix, max_iterations=30)
        print("DFS Path:", path_dfs)
        print("DFS Cost:", cost_dfs)
    except TimeoutException as e:
        print("DFS:", str(e))

    # Apel UCS
    try:
        path_ucs, cost_ucs = uniform_cost_search(distance_matrix, max_iterations=100000)
        print("UCS Path:", path_ucs)
        print("UCS Cost:", cost_ucs)
    except TimeoutException as e:
        print("UCS:", str(e))

    # Apel A*
    try:
        path_astar, cost_astar = a_star_search(distance_matrix, max_iterations=1150)
        print("A* Path:", path_astar)
        print("A* Cost:", cost_astar)
    except TimeoutException as e:
        print("A*:", str(e))






if __name__ == "__main__":
    main()
