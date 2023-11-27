from collections import deque
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def solve_cube_wo_heuristic(initial_state, solved_state, possible_moves, n):
    def is_goal_state(state):
        return state == solved_state

    visited_states = set()
    queue = deque([(initial_state, [])])
    initial_state_tuple = tuple(tuple(row) for face in initial_state for row in face)
    visited_states.add(initial_state_tuple)

    while queue:
        current_state, moves_so_far = queue.popleft()

        print("Current State:")
        display_cube(current_state)
        print("Moves So Far:", moves_so_far)
        print("-----------------------------------")

        if is_goal_state(current_state):
            return moves_so_far

        for move in possible_moves:
            new_state = apply_move(current_state, move, n)
            new_state_tuple = tuple(tuple(row) for face in new_state for row in face)

            if new_state_tuple not in visited_states:
                visited_states.add(new_state_tuple)
                new_moves = moves_so_far + [move]
                queue.append((new_state, new_moves))

    return None
