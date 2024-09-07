import matplotlib.pyplot as plt
import numpy as np

# Given points
point1 = (-6, 3)
point2 = (6, 4)
center = (0, 7/2)

# Compute radius from the center to one of the diameter endpoints
radius = np.linalg.norm(np.array(center) - np.array(point1))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the circle
circle = plt.Circle(center, radius, color='blue', fill=False, linestyle='--', label='Circle')
ax.add_artist(circle)

# Plot the diameter line segment
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='red', linestyle='-', marker='o', label='Diameter')

# Annotate the coordinates
plt.text(point1[0], point1[1], f'  {point1}', fontsize=12, ha='right', color='black')
plt.text(point2[0], point2[1], f'  {point2}', fontsize=12, ha='left', color='black')
plt.text(center[0], center[1], f'  {center}', fontsize=12, ha='center', color='black')

# Set equal scaling
ax.set_aspect('equal')

# Set limits for better view
ax.set_xlim(center[0] - radius - 1, center[0] + radius + 1)
ax.set_ylim(center[1] - radius - 1, center[1] + radius + 1)

# Add grid
plt.grid(True)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Circle with Diameter Line Segment')

# Add a legend
plt.legend()

# Show plot
plt.show()

