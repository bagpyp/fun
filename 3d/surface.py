import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the scalar function of two variables
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Generate the input data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and a colorbar
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.colorbar(ax.plot_surface(X, Y, Z), shrink=0.5)

# Customize the plot
ax.view_init(elev=40, azim=-70)

# Show the plot
plt.show()


