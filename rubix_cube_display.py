def display_cube(faces):
    for i in range(len(faces)):
        if i == 0:
            print("Left Face : ")
        elif i == 1:
            print("Top Face : ")
        elif i == 2:
            print("Right Face : ")
        elif i == 3:
            print("Bottom Face : ")
        elif i == 4:
            print("Back Face : ")
        else:
            print("Front Face : ")
        for j in range(len(faces[i])):
            print(faces[i][j])
        print()