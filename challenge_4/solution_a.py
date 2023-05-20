from itertools import combinations, chain, permutations

def bellman_ford(times):
    num_nodes = len(times)
    distances = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        distances[i][i] = times[i][i]
        for j in range(num_nodes):
            if i != j:
                distances[i][j] = times[i][j]
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances

def solution(times, time_limit):
    num_bunnies = len(times) - 2
    bunny_ids = list(range(num_bunnies))
    all_subsets = list(chain(*[combinations(bunny_ids, i+1) for i in range(num_bunnies)]))
    all_subsets.sort(key=len, reverse=True)
    shortest_distances = bellman_ford(times)

    # If negative cycle is present, we can save all bunnies
    for i in range(len(shortest_distances)):
        if shortest_distances[i][i] < 0:
            return bunny_ids

    for subset in all_subsets:
        for perm in permutations(subset):
            time_spent = shortest_distances[0][perm[0]+1] + shortest_distances[perm[-1]+1][-1]
            if len(perm) > 1:
                for i in range(len(perm)-1):
                    time_spent += shortest_distances[perm[i]+1][perm[i+1]+1]
            if time_spent <= time_limit:
                return sorted(list(perm))
    
    return []


# Test cases
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
# Output: [0, 1]

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
# Output: [1, 2]
