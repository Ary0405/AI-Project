# Necessary imports
import random
from rubix_cube_move import apply_move
from rubix_cube_display import display_cube

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

print("Initial State : ")
print()
display_cube(faces)

#Jumble karne ke liye number of moves input lere hai
scrambleMoves = int(input("How many moves you want for scrambling? "))

selectedMoves = random.choices(possibleMoves, k=scrambleMoves)

# Yaha se scramble karre hai
# Apply move khud code kara hai toh maybe koi error aaye isliye ek baar sab check karna
for move in selectedMoves:
    faces = apply_move(faces, move, n)


# final stae ko print karra hun after scrambling
print()
print("Final State : ")
print()
display_cube(faces)
