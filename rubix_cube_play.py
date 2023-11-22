# Necessary imports
import random
from rubix_cube_move import apply_move
from rubix_cube_display import display_cube
from collections import deque

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

print("Initial State : ")
print()
display_cube(faces)

# final stae ko print karra hun after scrambling
print("Final State : ")
print()
display_cube(scrambledCube)


def solve_cube(initial_state, solved_state, possible_moves, n):
    queue = deque([(initial_state, [])])

    while queue:
        current_state, moves_so_far = queue.popleft()

        print("Current State:")
        display_cube(current_state)
        print("Moves So Far:", moves_so_far)
        print("-------------------------")

        if current_state == solved_state:
            return moves_so_far

        for move in possible_moves:
            new_state = apply_move(current_state, move, n)
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
