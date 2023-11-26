import random
from rubix_cube_move import apply_move
from rubix_cube_patterndb import PatternDatabase
from rubix_cube_astar import a_star_solve_cube
from rubix_cube_heuristics import *

n = int(input("Please enter the value of n : "))

# Calculating number of moves that are possible for a n*n rubix cube
numberOfMoves = 0
helper = 0
if n % 2 == 0:
    numberOfMoves = (n / 2) * 12
    helper = n / 2
else:
    numberOfMoves = ((n - 1) / 2) * 12
    helper = (n - 1) / 2

# Finding all moves that are possible for a n*n rubix cube
generalMoves = ["R", "L", "T", "D", "F", "B"]
possibleMoves = []
for i in range(len(generalMoves)):
    for j in range(int(helper)):
        possibleMoves.append(generalMoves[i] + str(j) + "C")
        possibleMoves.append(generalMoves[i] + str(j) + "A")

# Creating a solved n*n rubix cube
colors = ["R", "G", "O", "B", "Y", "W"]
faces = []
for i in range(len(colors)):
    face = [[colors[i] for x in range(n)] for y in range(n)]
    faces.append(face)

# Taking input for number of times we need to scramble the cube
scrambleMoves = int(input("How many moves you want for scrambling? "))
selectedMoves = random.choices(possibleMoves, k=scrambleMoves)
scrambledCube = faces

with open('new.txt', 'w') as file:
    for move in selectedMoves:
        file.write("%s\n" % move)

# Scrambling the cube
middle_stages = []
for move in selectedMoves:
    scrambledCube = apply_move(scrambledCube, move, n)
    if selectedMoves.index(move) % 2 == 0:
            middle_stages.append(scrambledCube)

# Initializing pattern database
pattern_positions = generate_pattern_positions(n)
pattern_db = PatternDatabase(n, pattern_positions)

solved_state = faces

# Solving the cube
solution = []
for i in range(len(middle_stages) - 1, -1, -1):
    if i == len(middle_stages) - 1:
        solution = a_star_solve_cube(scrambledCube, middle_stages[i], possibleMoves, n, pattern_db, goal_pull_heuristic)
    else:
        temp_solution = a_star_solve_cube(middle_stages[i], middle_stages[i + 1], possibleMoves, n, pattern_db, goal_pull_heuristic)
        if temp_solution:
            solution += temp_solution

# Final solving
temp_solution = a_star_solve_cube(middle_stages[0], solved_state, possibleMoves, n, pattern_db, goal_pull_heuristic)
if temp_solution:
    solution += temp_solution

if solution:
    print("Solution found!")
    print("Sequence of moves:", solution)