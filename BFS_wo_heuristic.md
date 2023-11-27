# Rubik's Cube Solver using Breadth-First Search (BFS)

The Python code implements a solution algorithm for the Rubik's Cube, employing a Breadth-First Search (BFS) approach without the use of heuristics. The algorithm takes four main parameters: the initial state of the Rubik's Cube (`initial_state`), the solved state (`solved_state`), a set of possible moves (`possible_moves`), and the dimension of the cube (`n`).

## Algorithm Overview

The algorithm starts by initializing a queue and a set to keep track of visited states. The initial state, along with an empty list of moves, is enqueued into the queue. The algorithm then enters a while loop, continuing until the queue is empty or the solved state is reached. Within each iteration, the algorithm dequeues a state from the front of the queue, explores its neighboring states by applying each possible move, and enqueues the new states that have not been visited.

Throughout the process, the current state, moves performed so far, and a visual representation of the cube at each step are printed, providing insight into the algorithm's progress. The goal is to find a state that matches the solved state, at which point the sequence of moves leading to the solution is returned.

The BFS approach ensures optimality by systematically exploring states in a breadth-first manner, guaranteeing that the first solution found is the shortest possible sequence of moves to reach the solved state.

## Usage

To use the algorithm, call the `solve_cube_wo_heuristic` function with the initial state, solved state, possible moves, and cube dimension as arguments. The function returns the optimal sequence of moves to solve the Rubik's Cube.

```python
from collections import deque
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def solve_cube_wo_heuristic(initial_state, solved_state, possible_moves, n):
    # ... (code implementation)
    return optimal_moves
```

Note: The visual representation of the cube is displayed during the algorithm's execution for better understanding of the solving process.