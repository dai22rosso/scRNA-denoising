import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
#This file is for the tools of matrix and distance including:
#  plot matrix in gradient graph
#  convert lower triangle matrix to full matrix
#  normalize data to counts per num



def plot_gradient_matrix(matrix, lower_bound=1, upper_bound=10,mode=0,file_path='None'):
    """
    Plots a matrix with gradient colors.
    
    Parameters:
    - matrix: 2D numpy array, the input matrix to plot
    - lower_bound: int, the lower bound for the gradient color range
    - upper_bound: int, the upper bound for the gradient color range
    """
    # Define the color map
    if(mode==0):
        colors = ['blue'] + plt.cm.viridis(np.linspace(0, 1, upper_bound - lower_bound + 1)).tolist() + ['red']
        cmap = mcolors.ListedColormap(colors)

        # Define the bounds for colors
        bounds = [0, lower_bound] + list(range(lower_bound + 1, upper_bound + 1)) + [upper_bound + 1, matrix.max() + 1]
        norm = mcolors.BoundaryNorm(bounds, cmap.N)

        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 8))
        cbar = ax.imshow(matrix, cmap=cmap, norm=norm)
        fig.colorbar(cbar, ticks=bounds)

        # Set title and labels
        ax.set_title('Matrix Gradient Color Map')
        ax.set_xlabel('Features')
        ax.set_ylabel('Samples')
        if(file_path!='None'):
            plt.savefig(file_path)
        # Show the plot
        plt.show()
    elif mode == 1:
        if not (np.all(matrix >= 0) and np.all(matrix <= 1)):
            raise ValueError("All entries in the matrix must be between 0 and 1.")
        
        if not (0 <= lower_bound <= 1 and 0 <= upper_bound <= 1):
            raise ValueError("lower_bound and upper_bound must be between 0 and 1.")
        
        if lower_bound >= upper_bound:
            raise ValueError("lower_bound must be less than upper_bound.")
    
        # Define the color map
        cmap = plt.cm.viridis

        # Normalize the matrix based on the provided bounds
        norm = mcolors.Normalize(vmin=lower_bound, vmax=upper_bound)

        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 8))
        cbar = ax.imshow(matrix, cmap=cmap, norm=norm)
        fig.colorbar(cbar)

        # Set title and labels
        ax.set_title('Matrix Gradient Color Map')
        ax.set_xlabel('Features')
        ax.set_ylabel('Samples')
        if(file_path!='None'):
            plt.savefig(file_path)
        # Show the plot
        plt.show()
def LtoFull(m):
    """Convert lower triangle matrix to full matrix"""
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(i<j):
                m[i][j]=m[j][i]
    return m
def cp(array: np.ndarray,num) -> np.ndarray:
    """Normalize data to counts per num"""
    size_factors = array.sum(axis=1) / num
    normalized_array = array / size_factors[:, None]
    return normalized_array
