from rubix_cube_solver_astar import run_rubix_cube_solver
import csv

with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Value of N", "Scrambles", "Time Taken"])

while True:
    run_rubix_cube_solver()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
