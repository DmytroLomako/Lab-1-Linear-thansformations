import numpy as np
import matplotlib.pyplot as plt


X = np.array([
    [0, 3, 3, 1, 1, 2, 2, 1, 1, 0, 0],
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 0]
], dtype=float)

def draw_figure(X, X_modified = None, X_modified_label = None, title = "Original figure"):
    
    if X_modified is not None:
        if isinstance(X_modified, list):
            plt.plot(X[0], X[1], "--", color="gray", label = "Original")
            for result, label in zip(X_modified, X_modified_label):
                plt.plot(result[0], result[1], label=label)
        else:
            plt.plot(X[0], X[1], "--", label = "Original")
            plt.plot(X_modified[0], X_modified[1], marker = "o", label = X_modified_label)
    else:
        plt.plot(X[0], X[1], marker="o")
        
    plt.axis("equal")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    
    if X_modified is not None:
        plt.legend()
        
    plt.show()