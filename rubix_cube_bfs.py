from collections import deque
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def solve_cube(initial_state, solved_state, possible_moves, n, heuristic, pattern_db):
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

        if current_state == solved_state:
            return moves_so_far

        # Compute the heuristic value using the pattern database
        heuristic_value = pattern_db.compute_heuristic(current_state)
        queue = deque(
            sorted(
                queue,
                key=lambda x: len(x[1])
                + heuristic(x[0], solved_state)
                + heuristic_value,
            )
        )

        for move in possible_moves:
            new_state = apply_move(current_state, move, n)
            new_state_tuple = tuple(tuple(row) for face in new_state for row in face)

            if new_state_tuple not in visited_states:
                visited_states.add(new_state_tuple)
                new_moves = moves_so_far + [move]
                queue.append((new_state, new_moves))

    return None