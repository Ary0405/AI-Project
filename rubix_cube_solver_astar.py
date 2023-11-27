import random
from rubix_cube_bfs import solve_cube_with_heuristic
from rubix_cube_move import apply_move
from rubix_cube_patterndb import PatternDatabase
from rubix_cube_astar import a_star_solve_cube
from rubix_cube_heuristics import *
from rubix_cube_bfs_wo_heuristic import *
import time
import csv


def run_rubix_cube_solver():
    n = int(input("Please enter the value of n : "))
    # Calculating number of moves that are possible for a n*n rubix cube
    helper = 0
    if n % 2 == 0:
        helper = n / 2
    else:
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
    for move in selectedMoves:
        # print(move)
        scrambledCube = apply_move(scrambledCube, move, n)
        # print()
        # print(scrambledCube)
        # print()
        if selectedMoves.index(move) % 3 == 0:
            middle_stages.append(scrambledCube)

    # Initializing pattern database
    pattern_positions = generate_pattern_positions(n)
    pattern_db = PatternDatabase(n, pattern_positions)
    solved_state = faces

    # Solving the cube
    solution = []
    start_time = time.time()
    for i in range(len(middle_stages) - 1, -1, -1):
        if i == len(middle_stages) - 1:
            temp = a_star_solve_cube(
                scrambledCube,
                middle_stages[i],
                possibleMoves,
                n,
                pattern_db,
                heuristic_hamming_distance,
            )
            for move in temp:
                solution.append(move)
        else:
            temp = a_star_solve_cube(
                middle_stages[i + 1],
                middle_stages[i],
                possibleMoves,
                n,
                pattern_db,
                heuristic_hamming_distance,
            )
            for move in temp:
                solution.append(move)

    # Final solving
    temp_solution = a_star_solve_cube(
        middle_stages[0],
        solved_state,
        possibleMoves,
        n,
        pattern_db,
        heuristic_hamming_distance,
    )
    if temp_solution:
        for move in temp_solution:
            solution.append(move)
    end_time = time.time()

    if solution:
        print("Solution found!")
        print("Sequence of moves:", solution)

    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([n, scrambleMoves, end_time - start_time])
