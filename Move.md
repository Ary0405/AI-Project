# Rubik's Cube Rotation Code

This Python code is designed to simulate the rotation of a Rubik's Cube. It includes functions for rotating a subarray (representing a face of the cube) clockwise and counterclockwise. The primary function, `apply_move`, applies various Rubik's Cube moves to the cube.

## File Structure

The code is organized into the following sections:

1. **Import Module:** Importing the `rubix_cube_display` module, which presumably includes functionality for displaying the Rubik's Cube.

2. **Rotation Functions:**
   - `rotate_clockwise`: Rotates a given subarray (representing a cube face) clockwise.
   - `rotate_anticlockwise`: Rotates a given subarray anticlockwise.

3. **Color Definition:**
   - A list of color codes representing different colors on the Rubik's Cube.

4. **`apply_move` Function:**
   - Takes a Rubik's Cube, a move sequence, and the cube's dimension as input.
   - Applies various moves (`T`, `D`, `R`, `L`, `F`, `B`) to the cube based on the input move sequence.



## How to Use

1. **Import the Module:**
   - Make sure to import the `rubix_cube_display` module before using the functions.

2. **Define Colors:**
   - The `colors` list contains color codes used for representing different faces of the Rubik's Cube.

3. **Apply Moves:**
   - Use the `apply_move` function to simulate moves on the Rubik's Cube.
   - Provide the cube, move sequence, and dimension as arguments.

4. **Example Usage:**
   - final_state = apply_move(initial_state, move_string).

## Note

This code provides the basic structure for simulating Rubik's Cube rotations. The actual implementation of each move is left as a placeholder (indicated by comments). Users are encouraged to complete the implementation based on their specific requirements.

Feel free to explore and modify the code to suit your needs!
