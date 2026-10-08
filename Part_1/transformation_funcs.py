import numpy as np


def stretch(X, a, b):
    X_copy = X.copy()

    A = np.array([
        [a, 0],
        [0, b]
    ])

    X_new = A @ X_copy
    
    print("Stretch matrix:")
    print(A)

    return X_new

def shear(X, a, b):
    X_copy = X.copy()

    A = np.array([
        [1, a],
        [b, 1]
    ])

    X_new = A @ X_copy
    
    print("Shear matrix:")
    print(A)

    return X_new

def reflection(X, a, b):
    if a == 0 and b == 0:
        raise ValueError("Reflection direction cannot be (0, 0)")

    X_copy = X.copy()

    A = np.array([
        [a**2 - b**2, 2*a*b],
        [2*a*b, b**2 - a**2]
    ]) / (a**2 + b**2)

    X_new = A @ X_copy
    
    print("Reflection matrix:")
    print(A)

    return X_new

def rotation(X, theta):
    X_copy = X.copy()

    A = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    X_new = A @ X_copy
    
    print("Rotation matrix:")
    print(A)

    return X_new