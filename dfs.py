from timeout import timeout, TimeoutException


@timeout(300)
def depth_first_search(matrix, start=0, max_iterations=30):
    n = len(matrix)
    visited = [False] * n
    path = []
    best_path = []
    min_cost = float('inf')
    iteration = [0]

    def dfs(city, current_cost):
        nonlocal min_cost, best_path
        iteration[0] += 1
        if iteration[0] > max_iterations:
            raise TimeoutException("DFS a depășit numărul maxim de iterații permise")

        path.append(city)
        visited[city] = True

        if len(path) == n and matrix[city][start] > 0:
            total_cost = current_cost + matrix[city][start]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path.copy()
            print(f"DFS - Iteration {iteration[0]}: Current Path:", path, "Total Cost:", total_cost)
        else:
            for next_city in range(n):
                if not visited[next_city] and matrix[city][next_city] > 0:
                    dfs(next_city, current_cost + matrix[city][next_city])

        visited[city] = False
        path.pop()

    dfs(start, 0)
    return best_path, min_cost
