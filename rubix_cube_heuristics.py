def heuristic(cube, solved_state):
    distance = 0
    for face1, face2 in zip(cube, solved_state):
        for row1, row2 in zip(face1, face2):
            for color1, color2 in zip(row1, row2):
                if color1 != color2:
                    distance += 1
    return distance

def manhattan_distance(cubie1, cubie2):
    return sum(abs(coord1 - coord2) for coord1, coord2 in zip(cubie1, cubie2))

def cubie_to_numeric(cubie):
    color_mapping = {'R': 1, 'G': 2, 'B': 3, 'Y': 4, 'W': 5, 'O': 6}
    return tuple(color_mapping[color] for color in cubie)

def heuristic2(cube, solved_state):
    distance = 0
    for face1, face2 in zip(cube, solved_state):
        for cubie1, cubie2 in zip(face1, face2):
            if cubie1 != cubie2:
                distance += manhattan_distance(cubie_to_numeric(cubie1), cubie_to_numeric(cubie2))
    return distance

def generate_pattern_positions(n):
    pattern_positions = []
    center = n // 2  
    for i in range(center - 1, center + 2):
        for j in range(center - 1, center + 2):
            pattern_positions.append((i, j))
    return pattern_positions

def goal_pull_heuristic(cube, solved_state):
    distance = 0

    for face1, face2 in zip(cube, solved_state):
        for row1, row2 in zip(face1, face2):
            for color1, color2 in zip(row1, row2):
                if color1 != color2:
                    distance += goal_pull_distance(color1, color2)

    return distance

def goal_pull_distance(color1, color2):
    color_mapping = {'R': 0, 'G': 1, 'B': 2, 'Y': 3, 'W': 4, 'O': 5}
    return abs(color_mapping[color1] - color_mapping[color2])