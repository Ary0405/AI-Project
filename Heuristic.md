# Rubik's Cube Heuristic Functions

This Python code provides a set of heuristic functions designed for evaluating the state of a Rubik's Cube and determining its distance from the solved state.

## `heuristic_hamming_distance`

### Purpose:
Calculates the Hamming distance between the current cube state and the solved state. The Hamming distance is the count of positions at which the corresponding elements are different.

### Input:
- `cube`: The current state of the Rubik's Cube.
- `solved_state`: The solved state of the Rubik's Cube.

### Output:
- Returns the Hamming distance as an integer.

## `manhattan_distance`

### Purpose:
Calculates the Manhattan distance between two cubies. The Manhattan distance is the sum of the absolute differences of their corresponding coordinates.

### Input:
- `cubie1`, `cubie2`: Two cubies represented as tuples.

### Output:
- Returns the Manhattan distance as an integer.

## `cubie_to_numeric`

### Purpose:
Converts a cubie's color representation to numeric values based on a color mapping. This is useful for numerical comparison and distance calculation.

### Input:
- `cubie`: A cubie represented as a string.

### Output:
- Returns a tuple of numeric values representing the colors of the cubie.

## `heuristic2`

### Purpose:
Calculates a heuristic value based on the Manhattan distance of each cubie from the solved state. It provides a more refined evaluation of the cube state.

### Input:
- `cube`: The current state of the Rubik's Cube.
- `solved_state`: The solved state of the Rubik's Cube.

### Output:
- Returns the heuristic value as an integer.

## `generate_pattern_positions`

### Purpose:
Generates positions for a pattern on the Rubik's Cube. This function is helpful for defining specific patterns that are relevant to heuristic evaluation.

### Input:
- `n`: Dimension of the Rubik's Cube.

### Output:
- Returns a list of positions forming a pattern.

## `goal_pull_heuristic`

### Purpose:
Calculates a heuristic value based on the "goal-pull" distance between the colors of each position on the cube and the solved state. It reflects the effort required to pull each color toward its goal.

### Input:
- `cube`: The current state of the Rubik's Cube.
- `solved_state`: The solved state of the Rubik's Cube.

### Output:
- Returns the heuristic value as an integer.

## `goal_pull_distance`

### Purpose:
Calculates the "goal-pull" distance between two colors based on a predefined color mapping. This distance reflects the effort required to move from one color to another.

### Input:
- `color1`, `color2`: Two colors represented as strings.

### Output:
- Returns the "goal-pull" distance as an integer.
