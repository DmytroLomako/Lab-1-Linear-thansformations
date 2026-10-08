import os
import numpy as np


model_path = os.path.abspath("airplane_0001.off")
    
def read_off(filename):
    with open(filename, "r") as file:
        if file.readline().strip() != "OFF":
            raise ValueError("Not a valid OFF header")

        n_vertices, n_faces, n_edges = map(
            int, file.readline().split()
        )

        vertices = [
            list(map(float, file.readline().split()))
            for _ in range(n_vertices)
        ]

        faces = [
            list(map(int, file.readline().split()[1:]))
            for _ in range(n_faces)
        ]

    return np.array(vertices).T, faces


X_3d, faces = read_off(model_path)