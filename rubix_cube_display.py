def display_cube(faces):
    face_names = ["Left", "Top", "Right", "Bottom", "Back", "Front"]

    for i, face in enumerate(faces):
        print(f"{face_names[i]} Face:")
        for row in face:
            print(row)
        print()
