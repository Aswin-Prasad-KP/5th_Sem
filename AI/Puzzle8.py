import heapq

# (1, 2, 3)
# (4, 5, 6) => (1, 2, 3, 4, 5, 6, 7, 8, 0)
# (7, 8, 0)
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan_distance(state):
    distance = 0
    for index, tile in enumerate(state):
        if tile != 0:
            goal_index = GOAL_STATE.index(tile)
            current_row, current_col = divmod(index, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    zero_row, zero_col = divmod(zero_index, 3)
    def swap_and_create(new_zero_index):
        new_state = list(state)
        new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
        return tuple(new_state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for row_change, col_change in moves:
        new_row, new_col = zero_row + row_change, zero_col + col_change
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            neighbors.append(swap_and_create(new_zero_index))
    return neighbors

def best_first_search(start_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), start_state))
    came_from = {}
    came_from[start_state] = None
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == GOAL_STATE:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for neighbor in get_neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_list, (manhattan_distance(neighbor), neighbor))
    return None

# (1, 2, 3)
# (5, 6, 0) => (1, 2, 3, 5, 6, 0, 7, 8, 4)
# (7, 8, 4)

start_state = tuple(map(int, input().split()))
solution = best_first_search(start_state)
if solution:
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")