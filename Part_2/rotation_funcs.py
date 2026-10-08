import numpy as np


def rotate_xy(X, theta):
    X_copy = X.copy()

    A = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])

    X_new = A @ X_copy

    print("XY rotation matrix:")
    print(A)

    return X_new

def rotate_yz(X, theta):
    X_copy = X.copy()

    A = np.array([
        [1, 0,              0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])

    X_new = A @ X_copy

    print("YZ rotation matrix:")
    print(A)

    return X_new

def rotate_xz(X, theta):
    X_copy = X.copy()

    A = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0,             1,  0],
        [np.sin(theta), 0,  np.cos(theta)]
    ])

    X_new = A @ X_copy

    print("XZ rotation matrix:")
    print(A)

    return X_new