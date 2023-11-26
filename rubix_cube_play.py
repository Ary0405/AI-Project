import random
from rubix_cube_move import apply_move
from rubix_cube_patterndb import PatternDatabase
from rubix_cube_astar import a_star_solve_cube
from rubix_cube_heuristics import *
from rubix_cube_bidirect import bidirectional_search

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

# Scrambling the cube
middle_stages = []
no_of_middle_stages = 0
gap_between_stages = 0
if n < 5 :
    no_of_middle_stages = 1
    gap_between_stages = 3
elif n>5 and n < 7 :
    no_of_middle_stages = 2
    gap_between_stages = 2
elif n > 7  and n < 15:
    no_of_middle_stages = 3
    gap_between_stages = 3
else:
    no_of_middle_stages = 6
    gap_between_stages = 3

for move in selectedMoves:
    scrambledCube = apply_move(scrambledCube, move, n)
    if len(selectedMoves) > 10:
        if selectedMoves.index(move) % 2 == 0:
            middle_stages.append(scrambledCube)
    else :
        if selectedMoves.index(move) % 2 == 0:
            middle_stages.append(scrambledCube)

# Initializing pattern database
pattern_positions = generate_pattern_positions(n)
pattern_db = PatternDatabase(n, pattern_positions)

solved_state = faces
#solution = bidirectional_search(scrambledCube, solved_state, possibleMoves, n, pattern_db, heuristic)

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