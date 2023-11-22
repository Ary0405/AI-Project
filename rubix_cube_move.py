from rubix_cube_display import display_cube

def rotate_clockwise(subarray):
    transposed_subarray = [list(row) for row in zip(*subarray)]
    clockwise_rotated_subarray = [list(reversed(row)) for row in transposed_subarray]
    return clockwise_rotated_subarray


def rotate_anticlockwise(subarray):
    transposed_subarray = [list(row) for row in zip(*subarray)]
    anticlockwise_rotated_subarray = [
        list(row) for row in reversed(transposed_subarray)
    ]
    return anticlockwise_rotated_subarray

colors = ["R", "G", "O", "B", "Y", "W"]

def apply_move(cube, moves, n):
    new_cube_faces = []
    for i in range(len(colors)):
        face = [["#" for x in range(n)] for y in range(n)]
        new_cube_faces.append(face)

    if moves[0] == "T":
        side = int(moves[1])
        if moves[2] == "C":
            if side == 0:
                new_cube_faces[1] = rotate_clockwise(cube[1])

                new_cube_faces[0][0] = cube[5][0]
                new_cube_faces[5][0] = cube[2][0]
                new_cube_faces[2][0] = cube[4][0]
                new_cube_faces[4][0] = cube[0][0]

                new_cube_faces[3] = cube[3]
                new_cube_faces[0][1:] = cube[0][1:]
                new_cube_faces[2][1:] = cube[2][1:]
                new_cube_faces[4][1:] = cube[4][1:]
                new_cube_faces[5][1:] = cube[5][1:]
            else:
                new_cube_faces[0][side] = cube[5][side]
                new_cube_faces[4][side] = cube[0][side]
                new_cube_faces[2][side] = cube[4][side]
                new_cube_faces[5][side] = cube[2][side]

                new_cube_faces[3] = cube[3]
                new_cube_faces[1] = cube[1]

                new_cube_faces[0][0:side] = cube[0][0:side]
                new_cube_faces[2][0:side] = cube[2][0:side]
                new_cube_faces[4][0:side] = cube[4][0:side]
                new_cube_faces[5][0:side] = cube[5][0:side]

                new_cube_faces[0][side + 1 :] = cube[0][side + 1 :]
                new_cube_faces[2][side + 1 :] = cube[2][side + 1 :]
                new_cube_faces[4][side + 1 :] = cube[4][side + 1 :]
                new_cube_faces[5][side + 1 :] = cube[5][side + 1 :]
        else:
            if side == 0:
                new_cube_faces[1] = rotate_anticlockwise(cube[1])

                new_cube_faces[0][0] = cube[4][0]
                new_cube_faces[4][0] = cube[2][0]
                new_cube_faces[2][0] = cube[5][0]
                new_cube_faces[5][0] = cube[0][0]

                new_cube_faces[3] = cube[3]
                new_cube_faces[0][1:] = cube[0][1:]
                new_cube_faces[2][1:] = cube[2][1:]
                new_cube_faces[4][1:] = cube[4][1:]
                new_cube_faces[5][1:] = cube[5][1:]
            else:
                new_cube_faces[0][side] = cube[4][side]
                new_cube_faces[4][side] = cube[2][side]
                new_cube_faces[2][side] = cube[5][side]
                new_cube_faces[5][side] = cube[0][side]

                new_cube_faces[3] = cube[3]
                new_cube_faces[1] = cube[1]

                new_cube_faces[0][0:side] = cube[0][0:side]
                new_cube_faces[2][0:side] = cube[2][0:side]
                new_cube_faces[4][0:side] = cube[4][0:side]
                new_cube_faces[5][0:side] = cube[5][0:side]

                new_cube_faces[0][side + 1 :] = cube[0][side + 1 :]
                new_cube_faces[2][side + 1 :] = cube[2][side + 1 :]
                new_cube_faces[4][side + 1 :] = cube[4][side + 1 :]
                new_cube_faces[5][side + 1 :] = cube[5][side + 1 :]
    elif moves[0] == "D":
        side = int(moves[1])
        if moves[2] == "A":
            if side == 0:
                new_cube_faces[3] = rotate_anticlockwise(cube[3])

                new_cube_faces[0][n - 1] = cube[4][n - 1]
                new_cube_faces[4][n - 1] = cube[2][n - 1]
                new_cube_faces[2][n - 1] = cube[5][n - 1]
                new_cube_faces[5][n - 1] = cube[0][n - 1]

                new_cube_faces[1] = cube[1]

                new_cube_faces[0][0 : n - 1] = cube[0][0 : n - 1]
                new_cube_faces[2][0 : n - 1] = cube[2][0 : n - 1]
                new_cube_faces[4][0 : n - 1] = cube[4][0 : n - 1]
                new_cube_faces[5][0 : n - 1] = cube[5][0 : n - 1]
            else:
                new_cube_faces[3] = cube[3]
                new_cube_faces[1] = cube[1]

                new_cube_faces[0][n - 1 - side] = cube[4][n - 1 - side]
                new_cube_faces[4][n - 1 - side] = cube[2][n - 1 - side]
                new_cube_faces[2][n - 1 - side] = cube[5][n - 1 - side]
                new_cube_faces[5][n - 1 - side] = cube[0][n - 1 - side]

                new_cube_faces[0][0 : n - 1 - side] = cube[0][0 : n - 1 - side]
                new_cube_faces[4][0 : n - 1 - side] = cube[4][0 : n - 1 - side]
                new_cube_faces[2][0 : n - 1 - side] = cube[2][0 : n - 1 - side]
                new_cube_faces[5][0 : n - 1 - side] = cube[5][0 : n - 1 - side]

                new_cube_faces[0][n - side :] = cube[0][n - side :]
                new_cube_faces[4][n - side :] = cube[4][n - side :]
                new_cube_faces[2][n - side :] = cube[2][n - side :]
                new_cube_faces[5][n - side :] = cube[5][n - side :]
        else:
            if side == 0:
                new_cube_faces[3] = rotate_clockwise(cube[3])

                new_cube_faces[0][n-1] = cube[5][n-1]
                new_cube_faces[4][n-1] = cube[0][n-1]
                new_cube_faces[2][n-1] = cube[4][n-1]
                new_cube_faces[5][n-1] = cube[2][n-1]

                new_cube_faces[1] = cube[1]

                new_cube_faces[0][0:n-1] = cube[0][0:n-1]
                new_cube_faces[2][0:n-1] = cube[2][0:n-1]
                new_cube_faces[4][0:n-1] = cube[4][0:n-1]
                new_cube_faces[5][0:n-1] = cube[5][0:n-1]
            else:
                new_cube_faces[3] = cube[3]
                new_cube_faces[1] = cube[1]

                new_cube_faces[0][n - 1 - side] = cube[5][n - 1 - side]
                new_cube_faces[4][n - 1 - side] = cube[0][n - 1 - side]
                new_cube_faces[2][n - 1 - side] = cube[4][n - 1 - side]
                new_cube_faces[5][n - 1 - side] = cube[2][n - 1 - side]

                new_cube_faces[0][0 : n - 1 - side] = cube[0][0 : n - 1 - side]
                new_cube_faces[4][0 : n - 1 - side] = cube[4][0 : n - 1 - side]
                new_cube_faces[2][0 : n - 1 - side] = cube[2][0 : n - 1 - side]
                new_cube_faces[5][0 : n - 1 - side] = cube[5][0 : n - 1 - side]

                new_cube_faces[0][n - side :] = cube[0][n - side :]
                new_cube_faces[4][n - side :] = cube[4][n - side :]
                new_cube_faces[2][n - side :] = cube[2][n - side :]
                new_cube_faces[5][n - side :] = cube[5][n - side :]
    elif moves[0] == "R":
        side = int(moves[1])
        if moves[2] == "C":
            if side == 0:
                new_cube_faces[2] = rotate_anticlockwise(cube[2])
                for i in range(int(n)):
                    new_cube_faces[1][i][n - 1] = cube[4][i][n - 1]
                    new_cube_faces[4][i][n - 1] = cube[3][i][n - 1]
                    new_cube_faces[3][i][n - 1] = cube[5][i][n - 1]
                    new_cube_faces[5][i][n - 1] = cube[1][i][n - 1]

                new_cube_faces[0] = cube[0]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(int(n - 1)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
            else:
                for i in range(int(n)):
                    new_cube_faces[1][i][n - 1 - side] = cube[4][i][n - 1 - side]
                    new_cube_faces[4][i][n - 1 - side] = cube[3][i][n - 1 - side]
                    new_cube_faces[3][i][n - 1 - side] = cube[5][i][n - 1 - side]
                    new_cube_faces[5][i][n - 1 - side] = cube[1][i][n - 1 - side]

                new_cube_faces[0] = cube[0]
                new_cube_faces[2] = cube[2]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(0, int(n - 1 - side)):
                                new_cube_faces[face][i][j] = cube[face][i][j]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(int(n - side), int(n)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
        else:
            if side == 0:
                new_cube_faces[2] = rotate_clockwise(cube[2])
                for i in range(int(n)):
                    new_cube_faces[1][i][n - 1] = cube[5][i][n - 1]
                    new_cube_faces[4][i][n - 1] = cube[1][i][n - 1]
                    new_cube_faces[3][i][n - 1] = cube[4][i][n - 1]
                    new_cube_faces[5][i][n - 1] = cube[3][i][n - 1]

                new_cube_faces[0] = cube[0]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(int(n - 1)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
            else:
                for i in range(int(n)):
                    new_cube_faces[1][i][n - 1 - side] = cube[5][i][n - 1 - side]
                    new_cube_faces[4][i][n - 1 - side] = cube[1][i][n - 1 - side]
                    new_cube_faces[3][i][n - 1 - side] = cube[4][i][n - 1 - side]
                    new_cube_faces[5][i][n - 1 - side] = cube[3][i][n - 1 - side]

                new_cube_faces[0] = cube[0]
                new_cube_faces[2] = cube[2]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(0, int(n - 1 - side)):
                                new_cube_faces[face][i][j] = cube[face][i][j]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(int(n - side), int(n)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
    elif moves[0] == "L":
        side = int(moves[1])
        if moves[2] == "C":
            if side == 0:
                new_cube_faces[0] = rotate_clockwise(cube[0])
                for i in range(int(n)):
                    new_cube_faces[1][i][0] = cube[4][i][0]
                    new_cube_faces[4][i][0] = cube[3][i][0]
                    new_cube_faces[3][i][0] = cube[5][i][0]
                    new_cube_faces[5][i][0] = cube[1][i][0]

                new_cube_faces[2] = cube[2]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(1, int(n)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
            else:
                for i in range(int(n)):
                    new_cube_faces[1][i][side] = cube[4][i][side]
                    new_cube_faces[4][i][side] = cube[3][i][side]
                    new_cube_faces[3][i][side] = cube[5][i][side]
                    new_cube_faces[5][i][side] = cube[1][i][side]

                new_cube_faces[0] = cube[0]
                new_cube_faces[2] = cube[2]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(0, int(side)):
                                new_cube_faces[face][i][j] = cube[face][i][j]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(int(side + 1), int(n)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
        else:
            if side == 0:
                new_cube_faces[0] = rotate_anticlockwise(cube[0])
                for i in range(int(n)):
                    new_cube_faces[1][i][0] = cube[5][i][0]
                    new_cube_faces[4][i][0] = cube[1][i][0]
                    new_cube_faces[3][i][0] = cube[4][i][0]
                    new_cube_faces[5][i][0] = cube[3][i][0]

                new_cube_faces[2] = cube[2]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(1, int(n)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
            else:
                for i in range(int(n)):
                    new_cube_faces[1][i][side] = cube[5][i][side]
                    new_cube_faces[4][i][side] = cube[1][i][side]
                    new_cube_faces[3][i][side] = cube[4][i][side]
                    new_cube_faces[5][i][side] = cube[3][i][side]

                new_cube_faces[0] = cube[0]
                new_cube_faces[2] = cube[2]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(0, int(side)):
                                new_cube_faces[face][i][j] = cube[face][i][j]

                for face in range(len(colors)):
                    if face == 0 or face == 2:
                        continue
                    else:
                        for i in range(int(n)):
                            for j in range(int(side + 1), int(n)):
                                new_cube_faces[face][i][j] = cube[face][i][j]
    elif moves[0] == "F":
        side = int(moves[1])
        if moves[2] == "C":
            if side == 0:
                new_cube_faces[5] = rotate_clockwise(cube[5])
                new_cube_faces[4] = cube[4]

                last_column_matrix1 = [row[-1] for row in cube[0]]
                new_cube_faces[1][-1] = last_column_matrix1
                for i in range(int(n)):
                    new_cube_faces[2][i][0] = cube[1][-1][i]
                for i in range(int(n)):
                    new_cube_faces[3][-1][i] = cube[2][i][0]
                for i in range(int(n)):
                    new_cube_faces[0][i][-1] = cube[3][-1][i]

                # for face 1 and 3
                for i in range(0, int(n - 1)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(1, int(n)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(0, int(n - 1)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
            else:
                new_cube_faces[5] = cube[5]
                new_cube_faces[4] = cube[4]
                last_column_matrix1 = [row[-1 - side] for row in cube[0]]
                new_cube_faces[1][-1 - side] = last_column_matrix1
                for i in range(int(n)):
                    new_cube_faces[2][i][side] = cube[1][-1 - side][i]
                for i in range(int(n)):
                    new_cube_faces[3][-1 - side][i] = cube[2][i][side]
                for i in range(int(n)):
                    new_cube_faces[0][i][-1 - side] = cube[3][-1 - side][i]

                # for face 1 and 3
                for i in range(0, int(n - 1 - side)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]
                for i in range(int(n - side), int(n)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(0, int(side)):
                        new_cube_faces[2][i][j] = cube[2][i][j]
                for i in range(int(n)):
                    for j in range(int(side + 1), int(n)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(0, int(n - 1 - side)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
                for i in range(int(n)):
                    for j in range(int(n - side), int(n)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
        else:
            if side == 0:
                new_cube_faces[5] = rotate_anticlockwise(cube[5])
                new_cube_faces[4] = cube[4]
                for i in range(int(n)):
                    new_cube_faces[0][i][-1] = cube[1][-1][i]
                for i in range(int(n)):
                    new_cube_faces[1][-1][i] = cube[2][i][0]
                for i in range(int(n)):
                    new_cube_faces[2][i][0] = cube[3][-1][i]
                last_column_matrix1 = [row[-1] for row in cube[0]]
                new_cube_faces[3][-1] = last_column_matrix1

                # for face 1 and 3
                for i in range(0, int(n - 1)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(1, int(n)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(0, int(n - 1)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
            else:
                new_cube_faces[5] = cube[5]
                new_cube_faces[4] = cube[4]
                for i in range(int(n)):
                    new_cube_faces[0][i][-1 - side] = cube[1][-1 - side][i]
                for i in range(int(n)):
                    new_cube_faces[1][-1 - side][i] = cube[2][i][side]
                for i in range(int(n)):
                    new_cube_faces[2][i][side] = cube[3][-1 - side][i]
                last_column_matrix1 = [row[-1 - side] for row in cube[0]]
                new_cube_faces[3][-1 - side] = last_column_matrix1

                # for face 1 and 3
                for i in range(0, int(n - 1 - side)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]
                for i in range(int(n - side), int(n)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(0, int(side)):
                        new_cube_faces[2][i][j] = cube[2][i][j]
                for i in range(int(n)):
                    for j in range(side + 1, int(n)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(0, int(n - 1 - side)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
                for i in range(int(n)):
                    for j in range(int(n - side), int(n)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
    elif moves[0] == "B":
        side = int(moves[1])
        if moves[2] == "C":
            if side == 0:
                new_cube_faces[4] = rotate_clockwise(cube[4])
                new_cube_faces[5] = cube[5]

                for i in range(int(n)):
                    new_cube_faces[1][0][i] = cube[0][i][0]
                for i in range(int(n)):
                    new_cube_faces[2][i][-1] = cube[1][0][i]
                for i in range(int(n)):
                    new_cube_faces[3][0][i] = cube[2][i][-1]
                for i in range(int(n)):
                    new_cube_faces[0][i][0] = cube[3][0][i]

                # for face 1 and 3
                for i in range(1, int(n)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(0, int(n - 1)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(1, int(n)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
            else:
                new_cube_faces[5] = cube[5]
                new_cube_faces[4] = cube[4]
                for i in range(int(n)):
                    new_cube_faces[1][side][i] = cube[0][i][side]
                for i in range(int(n)):
                    new_cube_faces[2][i][-1 - side] = cube[1][side][i]
                for i in range(int(n)):
                    new_cube_faces[3][side][i] = cube[2][i][-1 - side]
                for i in range(int(n)):
                    new_cube_faces[0][i][side] = cube[3][side][i]

                # for face 1 and 3
                for i in range(0, int(side)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]
                for i in range(int(side + 1), int(n)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(0, int(n - 1 - side)):
                        new_cube_faces[2][i][j] = cube[2][i][j]
                for i in range(int(n)):
                    for j in range(int(n - side), int(n)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(0, int(side)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
                for i in range(int(n)):
                    for j in range(int(side + 1), int(n)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
        else:
            if side == 0:
                new_cube_faces[4] = rotate_anticlockwise(cube[4])
                new_cube_faces[5] = cube[5]

                for i in range(int(n)):
                    new_cube_faces[1][0][i] = cube[2][i][-1]
                for i in range(int(n)):
                    new_cube_faces[2][i][-1] = cube[3][0][i]
                for i in range(int(n)):
                    new_cube_faces[3][0][i] = cube[0][i][0]
                for i in range(int(n)):
                    new_cube_faces[0][i][0] = cube[1][0][i]

                # for face 1 and 3
                for i in range(1, int(n)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(0, int(n - 1)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(1, int(n)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
            else:
                new_cube_faces[4] = rotate_anticlockwise(cube[4])
                new_cube_faces[5] = cube[5]

                for i in range(int(n)):
                    new_cube_faces[1][side][i] = cube[2][i][-1 - side]
                for i in range(int(n)):
                    new_cube_faces[2][i][-1 - side] = cube[3][side][i]
                for i in range(int(n)):
                    new_cube_faces[3][side][i] = cube[0][i][side]
                for i in range(int(n)):
                    new_cube_faces[0][i][side] = cube[1][side][i]

                # for face 1 and 3
                for i in range(0, int(side)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]
                for i in range(int(side + 1), int(n)):
                    new_cube_faces[1][i] = cube[1][i]
                    new_cube_faces[3][i] = cube[3][i]

                # for face 2
                for i in range(int(n)):
                    for j in range(0, int(n - 1 - side)):
                        new_cube_faces[2][i][j] = cube[2][i][j]
                for i in range(int(n)):
                    for j in range(int(n - side), int(n)):
                        new_cube_faces[2][i][j] = cube[2][i][j]

                # for face 0
                for i in range(int(n)):
                    for j in range(0, int(side)):
                        new_cube_faces[0][i][j] = cube[0][i][j]
                for i in range(int(n)):
                    for j in range(int(side + 1), int(n)):
                        new_cube_faces[0][i][j] = cube[0][i][j]

    return new_cube_faces