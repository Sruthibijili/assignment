import matplotlib.pyplot as plt
import numpy as np

# Define the points
point1 = (-5, 4)
point2 = (-1, 6)

# Calculate the midpoint
midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Calculate the slope of the line segment
slope_line_segment = (point2[1] - point1[1]) / (point2[0] - point1[0])

# Calculate the slope of the perpendicular bisector
slope_perpendicular_bisector = -1 / slope_line_segment

# Define the range for x-values
x_values = np.linspace(min(point1[0], point2[0]) - 5, max(point1[0], point2[0]) + 5, 400)

# Calculate y-values for the line segment and perpendicular bisector
y_values_line_segment = slope_line_segment * (x_values - point1[0]) + point1[1]
y_values_perpendicular_bisector = slope_perpendicular_bisector * (x_values - midpoint[0]) + midpoint[1]

# Plotting
plt.figure(figsize=(10, 6))

# Plot the original points
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'ro', label='Points (-5, 4) and (-1, 6)')
plt.text(point1[0], point1[1], '(-5, 4)', fontsize=12, ha='right')
plt.text(point2[0], point2[1], '(-1, 6)', fontsize=12, ha='left')

# Plot the midpoint
plt.plot(midpoint[0], midpoint[1], 'bo', label='Midpoint (-3, 5)')
plt.text(midpoint[0], midpoint[1], f'(-3, 5)', fontsize=12, ha='left')

# Plot the line segment
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--', label='Line Segment')

# Plot the perpendicular bisector
plt.plot(x_values, y_values_perpendicular_bisector, 'm-', label='Perpendicular Bisector')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Points, Midpoint, and Perpendicular Bisector')
plt.legend()

# Show plot
plt.show()

