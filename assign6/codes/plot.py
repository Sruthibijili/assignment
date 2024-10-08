import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read direction cosines from data.txt
direction_cosines = []
with open('data.txt', 'r') as file:
    for line in file:
        print(f"Reading line: '{line.strip()}'")  # Debug: Show the line being read
        try:
            # Convert the line to a float and append it
            value = float(line.strip())
            direction_cosines.append(value)
        except ValueError:
            print(f"Invalid line, skipping: '{line.strip()}'")  # Debug: Invalid line

# Ensure we have exactly three direction cosines
if len(direction_cosines) != 3:
    raise ValueError(f"Expected exactly three direction cosines. Found: {len(direction_cosines)} values.")

# Extract direction cosines
l, m, n = direction_cosines

# Print the direction cosines
print(f"Direction Cosines: (l, m, n) = ({l:.2f}, {m:.2f}, {n:.2f})")

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Normalize direction cosines if necessary
length = np.sqrt(l**2 + m**2 + n**2)
l, m, n = l / length, m / length, n / length  # Normalize

# Plot the vector
ax.quiver(0, 0, 0, l, m, n, color='b', arrow_length_ratio=0.1)

# Set the limits based on the vector's normalized length
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Vector Plot')
ax.text(l/2, m/2, n/2, f'({l:.2f}, {m:.2f}, {n:.2f})', color='red')  # Add text for the vector

# Show the plot
plt.show()

