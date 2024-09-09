import matplotlib.pyplot as plt
import numpy as np
import re

def read_coordinates_from_file(file_path):
    """Reads coordinates from a file and returns a dictionary of points."""
    coordinates = {}
    pattern = re.compile(r'Point \d+: \(([-\d.]+),\s*([-\d.]+)\)')
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if "Point 1" in line:
                    match = pattern.search(line)
                    if match:
                        x, y = map(float, match.groups())
                        coordinates['Point 1'] = (x, y)
                elif "Point 2" in line:
                    match = pattern.search(line)
                    if match:
                        x, y = map(float, match.groups())
                        coordinates['Point 2'] = (x, y)
                elif "Midpoint" in line:
                    match = pattern.search(line)
                    if match:
                        x, y = map(float, match.groups())
                        coordinates['Midpoint'] = (x, y)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    print("Coordinates read from file:", coordinates)  # Debug print to verify data
    return coordinates

def calculate_midpoint(p1, p2):
    """Calculates the midpoint of two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def calculate_perpendicular_line(p1, p2, midpoint):
    """Calculates the coordinates of a perpendicular line."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    if dx == 0:  # Vertical line case
        return [midpoint[0], midpoint[0]], [midpoint[1] - 1, midpoint[1] + 1]
    if dy == 0:  # Horizontal line case
        return [midpoint[0] - 1, midpoint[0] + 1], [midpoint[1], midpoint[1]]
    
    slope = dy / dx
    perp_slope = -1 / slope
    intercept = midpoint[1] - perp_slope * midpoint[0]
    
    # Generate points for the perpendicular line
    x_vals = np.linspace(midpoint[0] - 1, midpoint[0] + 1, 100)
    y_vals = perp_slope * x_vals + intercept
    
    return x_vals, y_vals

def plot_data_and_perpendicular_line(coords):
    """Plots the coordinates, the line between Point 1 and Point 2, and the perpendicular line."""
    if 'Point 1' not in coords or 'Point 2' not in coords:
        print("Required points not found.")
        return
    
    p1 = coords['Point 1']
    p2 = coords['Point 2']
    midpoint = coords.get('Midpoint', calculate_midpoint(p1, p2))
    
    perp_x, perp_y = calculate_perpendicular_line(p1, p2, midpoint)
    
    plt.figure(figsize=(10, 8))
    
    # Plot points
    plt.scatter(*zip(*coords.values()), color='blue', label='Points')
    
    # Annotate points
    for label, (x, y) in coords.items():
        plt.text(x, y, f'{label} ({x}, {y})', fontsize=12, ha='right', color='blue')
    
    # Plot line between points
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', label='Line between Points')
    
    # Plot perpendicular line
    plt.plot(perp_x, perp_y, 'r--', label='Perpendicular Line')
    
    # Add title and labels
    plt.title('Plot of Coordinates and Perpendicular Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# Path to the data file (same folder as the script)
data_file_path = 'data.txt'

# Main execution
coords = read_coordinates_from_file(data_file_path)
plot_data_and_perpendicular_line(coords)
