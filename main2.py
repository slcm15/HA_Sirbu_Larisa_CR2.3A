
from dfs import depth_first_search, TimeoutException
from ucs import uniform_cost_search
from astar import a_star_search

def main2():
    simple_matrix=[[1,2,3],[4,5,6],[7,8,9]]
    # Apel DFS
    try:
        path_dfs, cost_dfs = depth_first_search(simple_matrix, max_iterations=30)
        print("DFS Path:", path_dfs)
        print("DFS Cost:", cost_dfs)
    except TimeoutException as e:
        print("DFS:", str(e))

    # Apel UCS
    try:
        path_ucs, cost_ucs = uniform_cost_search(simple_matrix, max_iterations=100000)
        print("UCS Path:", path_ucs)
        print("UCS Cost:", cost_ucs)
    except TimeoutException as e:
        print("UCS:", str(e))

    # Apel A*
    try:
        path_astar, cost_astar = a_star_search(simple_matrix, max_iterations=1150)
        print("A* Path:", path_astar)
        print("A* Cost:", cost_astar)
    except TimeoutException as e:
        print("A*:", str(e))

if __name__=="__main__":
    main2()

