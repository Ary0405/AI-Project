class PatternDatabase:
    def __init__(self, n, pattern_positions):
        self.n = n
        self.pattern_positions = pattern_positions
        self.database = {}

    def generate_pattern(self, cube_state):
        pattern = []

        for i, j in self.pattern_positions:
            if 0 <= i < len(cube_state) and 0 <= j < len(cube_state[0]):
                pattern.append(tuple(cube_state[i][j]))
            else:
                continue

        return tuple(pattern) 

    def compute_heuristic(self, cube_state):
        pattern = self.generate_pattern(cube_state)

        if pattern not in self.database:
            heuristic_value = self.compute_pattern_heuristic(cube_state)
            self.database[pattern] = heuristic_value

        return self.database[pattern]

    def compute_pattern_heuristic(self, cube_state):
        incorrect_count = 0

        for i, j in self.pattern_positions:
            if 0 <= i < len(cube_state) and 0 <= j < len(cube_state[0]):
                correct_color = self.get_correct_color_for_position(i, j, cube_state)
                if cube_state[i][j] != correct_color:
                    incorrect_count += 1

        return incorrect_count

    def get_correct_color_for_position(self, i, j, cube_state):
        try:
            return cube_state[i][j]
        except IndexError:
            return None
