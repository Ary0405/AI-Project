import random
from rubix_cube_move import apply_move
from rubix_cube_patterndb import PatternDatabase
from rubix_cube_astar import a_star_solve_cube

n = int(input("Please enter the value of n : "))

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

for i in range(len(generalMoves)):
    for j in range(int(helper)):
        possibleMoves.append(generalMoves[i] + str(j) + "C")
        possibleMoves.append(generalMoves[i] + str(j) + "A")

colors = ["R", "G", "O", "B", "Y", "W"]

faces = []
for i in range(len(colors)):
    face = [[colors[i] for x in range(n)] for y in range(n)]
    faces.append(face)


scrambleMoves = int(input("How many moves you want for scrambling? "))

selectedMoves = random.choices(possibleMoves, k=scrambleMoves)

scrambledCube = faces
for move in selectedMoves:
    scrambledCube = apply_move(scrambledCube, move, n)

def heuristic(cube, solved_state):
    distance = 0
    for face1, face2 in zip(cube, solved_state):
        for row1, row2 in zip(face1, face2):
            for color1, color2 in zip(row1, row2):
                if color1 != color2:
                    distance += 1
    return distance
def generate_pattern_positions(n):
    pattern_positions = []
    center = n // 2  # Find the center position for odd-sized cubes

    for i in range(center - 1, center + 2):
        for j in range(center - 1, center + 2):
            pattern_positions.append((i, j))

    return pattern_positions

pattern_positions = generate_pattern_positions(n)
pattern_db = PatternDatabase(n, pattern_positions)

solved_state = faces
solution = a_star_solve_cube(scrambledCube, solved_state, possibleMoves, n, pattern_db, heuristic)

if solution:
    print("Solution found!")
    print("Sequence of moves:", solution)
else:
    print("No solution found.")
