# Necessary imports
import random
from rubix_cube_move import apply_move
from rubix_cube_display import display_cube
from collections import deque
from all_states import rotate_cube, rotate_face
from heapq import heappop, heappush

# Input lere hai
n = int(input("Please enter the value of n : "))

# Number of possible moves calculated
numberOfMoves = 0
helper = 0
if n % 2 == 0:
    numberOfMoves = (n / 2) * 12
    helper = n / 2
else:
    numberOfMoves = ((n - 1) / 2) * 12
    helper = (n - 1) / 2


generalMoves = ["R", "L", "T", "D", "F", "B"]
possibleMoves = []

# Idhar se saare possible moves for n*n cube generate hore hai
for i in range(len(generalMoves)):
    for j in range(int(helper)):
        possibleMoves.append(generalMoves[i] + str(j) + "C")
        possibleMoves.append(generalMoves[i] + str(j) + "A")

colors = ["R", "G", "O", "B", "Y", "W"]

# Initial state of cube
faces = []
for i in range(len(colors)):
    face = [[colors[i] for x in range(n)] for y in range(n)]
    faces.append(face)


# Jumble karne ke liye number of moves input lere hai
scrambleMoves = int(input("How many moves you want for scrambling? "))

selectedMoves = random.choices(possibleMoves, k=scrambleMoves)

# Yaha se scramble karre hai
# Apply move khud code kara hai toh maybe koi error aaye isliye ek baar sab check karna
scrambledCube = faces
for move in selectedMoves:
    scrambledCube = apply_move(scrambledCube, move, n)

# print("Initial State : ")
# print()
# display_cube(faces)

# final stae ko print karra hun after scrambling
# print("Final State : ")
# print()
# display_cube(scrambledCube)

print(scrambledCube)


class PatternDatabase:
    def __init__(self, n, pattern_positions):
        self.n = n
        self.pattern_positions = pattern_positions
        self.database = {}

    def generate_pattern(self, cube_state):
        rows, cols = len(cube_state), len(cube_state[0])

        pattern = []
        try:
            pattern = tuple(tuple(cube_state[i][j]) for i, j in self.pattern_positions if 0 <= i < rows and 0 <= j < cols)
        except IndexError as e:
            print(f"Error generating pattern: {e}")

        return pattern

    def compute_heuristic(self, cube_state):
        pattern = self.generate_pattern(cube_state)

        # Convert the pattern to a tuple before using it as a key
        pattern = tuple(pattern)

        if pattern not in self.database:
            heuristic_value = self.compute_pattern_heuristic(cube_state, self.pattern_positions)
            self.database[pattern] = heuristic_value

        return self.database[pattern]

    def compute_pattern_heuristic(self, cube_state, pattern_positions):
        incorrect_count = 0

        for i, j in pattern_positions:
            if 0 <= i < len(cube_state) and 0 <= j < len(cube_state[0]):
                if cube_state[i][j] != "desired_color":
                    incorrect_count += 1

        return incorrect_count


def heuristic(cube, solved_state):
    distance = 0
    for face1, face2 in zip(cube, solved_state):
        for row1, row2 in zip(face1, face2):
            for color1, color2 in zip(row1, row2):
                if color1 != color2:
                    distance += 1
    return distance

pattern_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
pattern_db = PatternDatabase(n, pattern_positions)

def solve_cube(initial_state, solved_state, possible_moves, n):
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
            sorted(queue, key=lambda x: len(x[1]) + heuristic(x[0], solved_state) + heuristic_value)
        )

        for move in possible_moves:
            new_state = apply_move(current_state, move, n)
            new_state_tuple = tuple(tuple(row) for face in new_state for row in face)
            
            if new_state_tuple not in visited_states:
                visited_states.add(new_state_tuple)
                new_moves = moves_so_far + [move]
                queue.append((new_state, new_moves))

    return None



solved_state = faces
solution = solve_cube(scrambledCube, solved_state, possibleMoves, n)

if solution:
    print("Solution found!")
    print("Sequence of moves:", solution)
else:
    print("No solution found.")
