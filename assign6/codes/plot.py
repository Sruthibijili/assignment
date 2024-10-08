import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read angles from data.txt, handling non-numeric lines
angles = []
with open('data.txt', 'r') as file:
    for line in file:
        try:
            # Attempt to convert each line to a float
            angles.append(float(line.strip()))
        except ValueError:
            # If conversion fails, skip the line
            continue

# Ensure we have exactly three angles
if len(angles) != 3:
    raise ValueError("Expected exactly three angles in the file.")

# Extract angles (in degrees) and convert to radians
alpha, beta, gamma = np.radians(angles)  # Convert angles to radians

# Direction cosines
l = np.cos(alpha)
m = np.cos(beta)
n = np.cos(gamma)

# Calculate the length of the vector
vector_length = np.sqrt(l**2 + m**2 + n**2)

# Print the angles and direction cosines
print(f"Angles (in degrees): {angles}")
print(f"Direction Cosines: (l, m, n) = ({l:.2f}, {m:.2f}, {n:.2f})")

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector
ax.quiver(0, 0, 0, l, m, n, color='b', arrow_length_ratio=0.1)

# Set the limits based on the vector length
ax.set_xlim([0, l])
ax.set_ylim([0, m])
ax.set_zlim([0, n])

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Vector Plot')
ax.text(l/2, m/2, n/2, f'({l:.2f}, {m:.2f}, {n:.2f})', color='red')  # Add text for the vector

# Show the plot
plt.show()

