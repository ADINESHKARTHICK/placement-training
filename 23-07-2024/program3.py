def water_jug_problem(capacity1, capacity2, target):
    from collections import deque
    def is_valid_state(state):
        return (0 <= state[0] <= capacity1) and (0 <= state[1] <= capacity2)  
    def get_successors(state):
        jug1, jug2 = state
        return [
            (capacity1, jug2),  # Fill Jug1
            (jug1, capacity2),  # Fill Jug2
            (0, jug2),  # Empty Jug1
            (jug1, 0),  # Empty Jug2
            (min(jug1 + jug2, capacity1), max(0, jug2 - (capacity1 - jug1))),  # Pour Jug2 to Jug1
            (max(0, jug1 - (capacity2 - jug2)), min(jug1 + jug2, capacity2))   # Pour Jug1 to Jug2
        ]    
    stack = [(0, 0)]
    visited = set()
    path = []   
    while stack:
        current_state = stack.pop()
        if current_state in visited:
            continue
        visited.add(current_state)
        path.append(current_state)
        
        jug1, jug2 = current_state
        if jug1 == target or jug2 == target:
            return path
        
        for next_state in get_successors(current_state):
            if is_valid_state(next_state):
                stack.append(next_state)    
    return None
if path_to_solution:
    print("Path to solution:", path_to_solution)
else:
    print("No solution found.")
