# Necessary imports
import random
from rubix_cube_move import apply_move
from rubix_cube_display import display_cube
from collections import deque
from all_states import rotate_cube, rotate_face

# Input lere hai
n = int(input("Please enter the value of n: "))

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

# Generate all possible solved states including rotations
solved_states = rotate_cube(faces)
for state in solved_states:
    print("rirgirngirngirng")
    display_cube(state)

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

# final state ko print karra hun after scrambling
print("Final State : ")
print()
display_cube(scrambledCube)




def heuristic(cube, reference_solved_state):
    distance = 0
    for face1, face2 in zip(cube, reference_solved_state):
        for row1, row2 in zip(face1, face2):
            for color1, color2 in zip(row1, row2):
                if color1 != color2:
                    distance += 1
    return distance

def solve_cube(initial_state, solved_states, possible_moves, n):
    queue = deque([(initial_state, [])])

    while queue:
        queue = deque(sorted(queue, key=lambda x: len(x[1]) + heuristic(x[0], solved_states[0])))

        current_state, moves_so_far = queue.popleft()

        print("Current State:")
        display_cube(current_state)
        print("Moves So Far:", moves_so_far)
        print("-------------------------")

        if current_state in solved_states:
            return moves_so_far

        for move in possible_moves:
            new_state = apply_move(current_state, move, n)
            new_moves = moves_so_far + [move]

            queue.append((new_state, new_moves))

        for e in queue:
            print(e[0])
        
        exit()

    return None

# solution = solve_cube(scrambledCube, solved_states, possibleMoves, n)

# if solution:
#     print("Solution found!")
#     print("Sequence of moves:", solution)
# else:
#     print("No solution found.")
# print('--------------------')

# cube1 = apply_move(scrambledCube,'T0C',n)
# display_cube(cube1)
# print('--------------------')
# display_cube(scrambledCube)
# print('--------------------')

# display_cube(apply_move(scrambledCube,'T0A',n))