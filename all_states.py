from itertools import product

def rotate_cube(initial_state):
    rotated_states = []

    # Iterate over all possible rotations for each face
    for rotations in product([0, 90, 180, -90], repeat=6):  # 6 faces
        rotated_cube = [rotate_face(face, rotation) for face, rotation in zip(initial_state, rotations)]
        rotated_states.append(rotated_cube)

    return rotated_states

def rotate_face(face, rotation):
    n = len(face)
    rotated_face = [[None] * n for _ in range(n)]

    if rotation == 0:
        return face

    if rotation > 0:
        for i in range(n):
            for j in range(n):
                rotated_face[j][n - 1 - i] = face[i][j]
    else:  # rotation < 0
        for i in range(n):
            for j in range(n):
                rotated_face[n - 1 - j][i] = face[i][j]

    return rotated_face