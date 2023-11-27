from collections import deque
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def solve_cube_with_heuristic(initial_state, solved_state, possible_moves, n, heuristic):
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

        # Generate successors and sort them based on the heuristic value
        successors = [(apply_move(current_state, move, n), moves_so_far + [move]) for move in possible_moves]
        successors.sort(key=lambda x: heuristic(x[0], solved_state))

        for new_state, new_moves in successors:
            new_state_tuple = tuple(tuple(row) for face in new_state for row in face)

            if new_state_tuple not in visited_states:
                visited_states.add(new_state_tuple)
                queue.append((new_state, new_moves))

    return None
