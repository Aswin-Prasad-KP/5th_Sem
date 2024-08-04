import heapq

class WaterBucketProblem:
    def __init__(self, capacity1, capacity2, goal):
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.goal = goal
        self.visited = set()

    def heuristic(self, state):
        bucket1, bucket2 = state
        return abs(self.goal - (bucket1 + bucket2))

    def is_goal(self, state):
        bucket1, bucket2 = state
        return bucket1 == self.goal or bucket2 == self.goal or bucket1 + bucket2 == self.goal

    def get_neighbors(self, state):
        bucket1, bucket2 = state
        neighbors = []
        neighbors.append((self.capacity1, bucket2))
        neighbors.append((bucket1, self.capacity2))
        neighbors.append((0, bucket2))
        neighbors.append((bucket1, 0))
        pour_to_2 = min(bucket1, self.capacity2 - bucket2)
        neighbors.append((bucket1 - pour_to_2, bucket2 + pour_to_2))
        pour_to_1 = min(bucket2, self.capacity1 - bucket1)
        neighbors.append((bucket1 + pour_to_1, bucket2 - pour_to_1))
        return neighbors

    def solve(self):
        initial_state = (0, 0)
        pq = []
        heapq.heappush(pq, (self.heuristic(initial_state), 0, initial_state))
        while pq:
            _, cost, current = heapq.heappop(pq)
            if self.is_goal(current):
                return cost, current
            if current in self.visited:
                continue
            self.visited.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    heapq.heappush(pq, (self.heuristic(neighbor), cost + 1, neighbor))
        return None

def main():
    capacity1 = int(input("Enter capacity of bucket 1: "))
    capacity2 = int(input("Enter capacity of bucket 2: "))
    goal = int(input("Enter the goal amount of water: "))
    problem = WaterBucketProblem(capacity1, capacity2, goal)
    solution = problem.solve()
    if solution:
        print(f"Steps to reach goal: {solution[0]}, Final state: {solution[1]}")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()