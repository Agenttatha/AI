from collections import deque

def pour(state, jug1, jug2):
   
    amt = min(state[jug1], (jug_caps[jug2] - state[jug2]))
    new_state = list(state)
    new_state[jug1] -= amt
    new_state[jug2] += amt
    return tuple(new_state)

def get_successors(state):
    
    successors = []
    for jug1, jug2 in [(0, 1), (1, 0)]:
        new_state = pour(state, jug1, jug2)
        if new_state != state:
            successors.append(new_state)
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = jug_caps[jug]
        successors.append(tuple(new_state))
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = 0
        successors.append(tuple(new_state))
    return successors

def heuristic(state, goal):

    return sum(abs(state[i] - goal[i]) for i in range(len(state)))

def a_star(start, goal):
   
    open_list = [(heuristic(start, goal), start)]
    print(open_list)
    closed_list = set()
    parent = {start: None}
    while open_list:
        _, curr_state = open_list.pop(0)
        if curr_state == goal:
            path = deque()
            state = curr_state
            while state is not None:
                path.appendleft(state)
                state = parent[state]
            return list(path)
        closed_list.add(curr_state)
        for succ_state in get_successors(curr_state):
            if succ_state not in closed_list:
                succ_cost = heuristic(succ_state, goal)
                open_list.append((succ_cost, succ_state))
                open_list.sort()
                parent[succ_state] = curr_state
    return None

jug_caps = (4, 3)
start_state = (0, 0)
goal_state = (2, 0)

solution = a_star(start_state, goal_state)
if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution exists.")
