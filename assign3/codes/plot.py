import matplotlib.pyplot as plt
import numpy as np

def calculate_midpoint(point1, point2):
    """Calculate the midpoint between two points."""
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def calculate_radius(center, point):
    """Calculate the radius of the circle given the center and a point on the circle."""
    return np.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)

def plot_circle(ax, center, radius):
    """Plot a circle given the center and radius."""
    circle = plt.Circle(center, radius, color='green', fill=False, linestyle='--', linewidth=1.5, label='Circle')
    ax.add_patch(circle)

def plot_line(ax, point1, point2):
    """Plot a line segment between two points."""
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    ax.plot(x_values, y_values, color='blue', linestyle='-', linewidth=1.5, label='Line Segment')

def plot_points_and_circle(points, center):
    """Plot points, center, line segment, and circle on a scatter plot."""
    x_vals, y_vals = zip(*points)
    midpoint = calculate_midpoint(points[0], points[1])
    radius = calculate_radius(center, points[0])  # Use distance from center to one of the points as radius

    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot points
    ax.scatter(x_vals, y_vals, color='blue', label='Points')
    
    # Plot center
    ax.scatter(center[0], center[1], color='red', label='Center', marker='x', s=100)
    
    # Plot the circle
    plot_circle(ax, center, radius)
    
    # Plot the line segment
    plot_line(ax, points[0], points[1])
    
    # Plot midpoint
    ax.scatter(midpoint[0], midpoint[1], color='purple', label='Midpoint', marker='o', s=100)
    
    # Annotate points, center, and midpoint
    for (x, y) in points:
        ax.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    ax.annotate(f'Center\n({center[0]:.2f}, {center[1]:.2f})', center, textcoords="offset points", xytext=(0,10), ha='center')
    ax.annotate(f'Midpoint\n({midpoint[0]:.2f}, {midpoint[1]:.2f})', midpoint, textcoords="offset points", xytext=(0,10), ha='center')
    
    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plot of Points, Circle, Line Segment, Center, and Midpoint')
    ax.legend()
    ax.grid(True)
    
    # Set equal scaling
    ax.set_aspect('equal', 'box')
    
    # Show plot
    plt.show()

if __name__ == "__main__":
    # Define the points and calculate the center
    points = [(-6, 3), (6, 4)]
    center = calculate_midpoint(points[0], points[1])
    
    # Plot the points, center, circle, line segment, and midpoint
    plot_points_and_circle(points, center)


