import heapq
from timeout import timeout, TimeoutException

@timeout(300)
def uniform_cost_search(matrix, start=0, max_iterations=100000):
    n = len(matrix)
    pq = []
    heapq.heappush(pq, (0, [start]))
    best_cost = float('inf')
    best_path = []

    iteration = 0
    while pq:
        iteration += 1
        if iteration > max_iterations:
            print("UCS a depășit numărul maxim de iterații permise.")
            break

        current_cost, path = heapq.heappop(pq)
        current_city = path[-1]


        if len(path) > 1 and path[-1] == start and len(path) == n + 1:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path
            continue


        for next_city in range(n):
            if next_city not in path or (next_city == start and len(path) == n):
                next_path = path + [next_city]
                next_cost = current_cost + matrix[current_city][next_city]
                heapq.heappush(pq, (next_cost, next_path))

        if iteration % 10000 == 0:
            print(f"UCS - Iteration {iteration}: Current Path: {path}, Cost: {current_cost}")

    if best_path == []:
        best_path = path
        best_cost = current_cost

    return best_path, best_cost
