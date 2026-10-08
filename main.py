import numpy as np
import matplotlib.pyplot as plt
from Part_1.transformation_funcs import stretch, shear, reflection, rotation
from Part_1.matrix import draw_figure, X
from Part_1.combinations import run_sequence
from Part_2.rotation_funcs import rotate_xy, rotate_yz, rotate_xz
from Part_2.file_handler import X_3d, faces
from Part_2.display_3d import plot_3d, visualize_off

if __name__ == "__main__":
    
    draw_figure(X)
    theta = np.deg2rad(45)


    # PART 1
    
    X_stretched = stretch(X, 2, 0.5)
    draw_figure(X, X_stretched, "Stretched", "Stretch: a=2, b=0.5")

    X_sheared = shear(X, 0.5, 0)
    draw_figure(X, X_sheared, "Sheared", "Shear: a=0.5, b=0")

    X_reflected = reflection(X, 1, 1)
    draw_figure(X, X_reflected, "Reflected", "Reflection across y = x")

    X_rotated = rotation(X, np.deg2rad(45))
    draw_figure(X, X_rotated, "Rotated", "Rotation: 45 degrees")
    
    
    
    # PART 2

    S = np.array([[2, 0], [0, 0.5]])

    H = np.array([[1, 0.5],[0, 1]])

    R = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta),  np.cos(theta)]])
    
    stretch_step = ("Stretch", stretch, (2, 0.5), S)
    shear_step = ("Shear", shear, (0.5, 0), H)
    rotation_step = ("Rotation", rotation, (theta,), R)

    result_1 = run_sequence(
        X,
        [stretch_step, shear_step, rotation_step],
        "Stretch -> Shear -> Rotation"
    )

    result_2 = run_sequence(
        X,
        [shear_step, stretch_step, rotation_step],
        "Shear -> Stretch -> Rotation"
    )

    result_3 = run_sequence(
        X,
        [rotation_step, stretch_step, shear_step],
        "Rotation -> Stretch -> Shear"
    )

    result_4 = run_sequence(
        X,
        [stretch_step, rotation_step, shear_step],
        "Stretch -> Rotation -> Shear"
    )

    draw_figure(
        X, 
        [result_1, result_2, result_3, result_4],
        ["Stretch -> Shear -> Rotation", "Shear -> Stretch -> Rotation", "Rotation -> Stretch -> Shear", "Stretch -> Rotation -> Shear"], 
        "Comparison of transformation orders"
    )
    
    
    
    # PART 3
    
    visualize_off(X_3d, faces)
    # plot_3d(X_3d, faces, "Original 3D model")

    X_rotated_xy = rotate_xy(X_3d, theta)
    visualize_off(X_rotated_xy, faces)
    # plot_3d(X_rotated_xy, faces, "XY rotation: 45 degrees")
    
    X_rotated_yz = rotate_yz(X_3d, np.deg2rad(45))
    visualize_off(X_rotated_yz, faces)
    # plot_3d(X_rotated_yz, faces, "YZ rotation: 45 degrees")
    
    X_rotated_xz = rotate_xz(X_3d, np.deg2rad(45))
    visualize_off(X_rotated_xz, faces)
    # plot_3d(X_rotated_xz, faces, "XZ rotation: 45 degrees")
    
    
    
    # PART 4

    X1 = rotate_xy(X_3d, theta)
    X2 = rotate_yz(X1, theta)
    X3 = rotate_xz(X2, theta)

    R_xy = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])

    R_yz = np.array([
        [1, 0,              0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])

    R_xz = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0,             1,  0],
        [np.sin(theta), 0,  np.cos(theta)]
    ])

    A_total = R_xz @ R_yz @ R_xy
    
    print("Combined rotation matrix (XZ -> YZ -> XY):")
    print(A_total)

    # plot_3d(X3, faces, "Combined rotations: XY -> YZ -> XZ")
    visualize_off(X3, faces)