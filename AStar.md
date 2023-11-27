# A* Search with Pattern Database for Rubik's Cube Solver

This Python code implements an A* search algorithm for solving the Rubik's Cube, incorporating a pattern database (pattern_db) and a heuristic function. The algorithm aims to find the optimal sequence of moves from an initial state to a solved state, considering a set of possible moves, the cube's dimension, and a pattern database.

## Algorithm Overview

The `a_star_solve_cube` function utilizes a priority queue to prioritize states based on a combined cost function. The cost function is computed as the sum of the following three components:
1. The length of moves performed so far.
2. The heuristic value of the current state compared to the solved state.
3. The heuristic value computed from the pattern database (`pattern_db.compute_heuristic`).

The priority queue is initially populated with the initial state, an empty list of moves, and a priority value of 0. The algorithm continues until the priority queue is empty or the solved state is reached. During each iteration, the state, sequence of moves so far, and a visual representation of the cube are printed for better understanding.

If the current state matches the solved state, the function returns the optimal sequence of moves. Otherwise, the algorithm explores successors by applying each possible move to the current state, ensuring that new states are not revisited. Successors are enqueued into the priority queue with updated costs based on the computed cost function.

## Usage

To use the algorithm, call the `a_star_solve_cube` function with appropriate arguments, including the initial state, solved state, possible moves, cube dimension, pattern database, and a heuristic function. The function returns the optimal sequence of moves to solve the Rubik's Cube.

```python
from queue import PriorityQueue
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def a_star_solve_cube(initial_state, solved_state, possible_moves, n, pattern_db, heuristic):
    # ... (code implementation)
    return optimal_moves
```

Note: The visual representation of the cube is displayed during the algorithm's execution, providing insights into the solving process guided by the A* search algorithm and pattern database heuristic.