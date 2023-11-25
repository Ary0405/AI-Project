from queue import PriorityQueue
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def a_star_solve_cube(initial_state, solved_state, possible_moves, n, pattern_db, heuristic):
    def compute_cost(cube, moves_so_far):
        heuristic_val = pattern_db.compute_heuristic(current_state)
        return len(moves_so_far) + heuristic(cube, solved_state) + heuristic_val

    visited_states = set()
    priority_queue = PriorityQueue()
    initial_state_tuple = tuple(tuple(row) for face in initial_state for row in face)
    visited_states.add(initial_state_tuple)

    priority_queue.put((0, initial_state, []))  # Priority is initially set to 0
    while not priority_queue.empty():
        _, current_state, moves_so_far = priority_queue.get()

        print("Current State:")
        display_cube(current_state)
        print("Moves So Far:", moves_so_far)
        print("-----------------------------------")

        if current_state == solved_state:
            return moves_so_far

        for move in possible_moves:
            new_state = apply_move(current_state, move, n)
            new_state_tuple = tuple(tuple(row) for face in new_state for row in face)

            if new_state_tuple not in visited_states:
                visited_states.add(new_state_tuple)
                new_moves = moves_so_far + [move]
                cost = compute_cost(new_state, new_moves)
                priority_queue.put((cost, new_state, new_moves))

    return None