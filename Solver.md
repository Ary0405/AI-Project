# Rubik's Cube Solver

The provided Python script is a Rubik's Cube solver. Let's break down the script into sections for better understanding.

## Input Section

1. **Cube Dimensions:**
   - The user is prompted to enter the dimension (`n`) of the Rubik's Cube.

2. **Possible Moves:**
   - Calculates and generates possible moves based on the cube dimension.

3. **Scrambling:**
   - The script scrambles a solved Rubik's Cube by applying randomly selected moves.

## Rubik's Cube Initialization

1. **Solved Cube:**
   - Initializes a solved Rubik's Cube with faces of different colors.

2. **Scrambling:**
   - Randomly selects moves and applies them to scramble the cube.

## Pattern Database Initialization

1. **Pattern Positions:**
   - Generates pattern positions based on the cube dimension.

2. **Pattern Database:**
   - Initializes a pattern database (`PatternDatabase` class) to store and manage patterns.

## Solving the Cube

1. **Middle Stages Logic:**
   - The script introduces a concept of "middle stages" during the solving process.
   - For each third move during scrambling, an intermediate state of the cube is saved.
   - This allows the solver to efficiently solve the cube by dividing it into smaller, more manageable sections.

2. **A* Search Algorithm:**
   - Utilizes the A* search algorithm to solve the Rubik's Cube.
   - Solves the cube in reverse order, from the last scrambled state to the initial state.
   - Uses the `heuristic_hamming_distance (can be changed)` function for heuristic evaluation.

3. **Performance Measurement:**
   - Measures the time taken to solve the cube and writes the results to a CSV file (`results.csv`).

## Output

1. **Solution:**
   - If a solution is found, it prints the sequence of moves.

2. **CSV File:**
   - Records cube dimension, scramble moves, and solving time in the `results.csv` file.

This script provides a basic Rubik's Cube solving implementation using the A* search algorithm with a Hamming distance heuristic. The introduction of "middle stages" enhances the solving efficiency by breaking down the cube into smaller sections. It's a simplified example for educational purposes, and there are more advanced algorithms and heuristics for solving Rubik's Cubes efficiently.