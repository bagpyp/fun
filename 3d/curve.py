import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate some data
t = np.linspace(-4*np.pi, 4*np.pi, 500)
x = np.sin(t)
y = np.cos(t)
z = t

# Plot the data as a 3D curve
ax.plot(x, y, z, label='3D curve')

# Add labels and a legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Customize the plot
ax.view_init(elev=20, azim=-70)

# Show the plot
plt.show()

