import heapq
from collections import deque

class Puzzle:
    def _init_(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.n = 3
    def find_zero(self, state):
        return state.index(0)
    def valid_moves(self, zero_index):
        moves = []
        row, col = zero_index // self.n, zero_index % self.n
        if row > 0:
            moves.append(-self.n)  # Up
        if row < self.n - 1:
            moves.append(self.n)   # Down
        if col > 0:
            moves.append(-1)       # Left
        if col < self.n - 1:
            moves.append(1)        # Right
        return moves
    def apply_move(self, state, move):
        zero_index = self.find_zero(state)
        new_index = zero_index + move
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        return tuple(new_state)

    def bfs(self):
        queue = deque([(self.initial_state, [])])
        visited = set()
        while queue:
            state, path = queue.popleft()
            if state == self.goal_state:
                return path
            zero_index = self.find_zero(state)
            for move in self.valid_moves(zero_index):
                new_state = self.apply_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))
        return None

    def dfs(self):
        stack = [(self.initial_state, [])]
        visited = set()
        while stack:
            state, path = stack.pop()
            if state == self.goal_state:
                return path
            zero_index = self.find_zero(state)
            for move in self.valid_moves(zero_index):
                new_state = self.apply_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    stack.append((new_state, path + [new_state]))
        return None

    def h(self, state):
        # Heuristic: Sum of Manhattan distances
        return sum(abs((val-1) % self.n - idx % self.n) + abs((val-1) // self.n - idx // self.n)
                   for idx, val in enumerate(state) if val != 0)

    def a_star(self):
        heap = [(self.h(self.initial_state), self.initial_state, [])]
        visited = set()
        while heap:
            _, state, path = heapq.heappop(heap)
            if state == self.goal_state:
                return path
            zero_index = self.find_zero(state)
            for move in self.valid_moves(zero_index):
                new_state = self.apply_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    heapq.heappush(heap, (self.h(new_state) + len(path) + 1, new_state, path + [new_state]))
        return None

def display_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print(f"Solution found in {len(solution)} moves.")
        for step in solution:
            display_state(step)

def display_state(state):
    n = 3
    for i in range(n):
        print(state[i*n:(i+1)*n])
    print()
def get_user_input():
    print("Enter the initial state of the 8-puzzle in row-major order (use 0 for the blank space):")
    initial_state = tuple(map(int, input().split()))
    if len(initial_state) != 9 or set(initial_state) != set(range(9)):
        raise ValueError("Invalid input! Please enter exactly 9 numbers from 0 to 8.")
    return initial_state
def main():
    initial_state = get_user_input()
    puzzle = Puzzle(initial_state)

    print("Select algorithm to solve the puzzle (bfs, dfs, a*):")
    algo = input().strip().lower()

    if algo == "bfs":
        solution = puzzle.bfs()
    elif algo == "dfs":
        solution = puzzle.dfs()
    elif algo == "a*":
        solution = puzzle.a_star()
    else:
        print("Invalid algorithm selection.")
        return

    display_solution(solution)
if _name_ == "_main_":
    main()
