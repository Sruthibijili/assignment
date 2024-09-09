import math
import re
import matplotlib.pyplot as plt

def read_coordinates_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        
        # Regular expressions to find the coordinates
        pattern = r'Point 1:\s*\((-?\d+\.?\d*),\s*(-?\d+\.?\d*)\)\s*' \
                  r'Point 2:\s*\((-?\d+\.?\d*),\s*(-?\d+\.?\d*)\)\s*' \
                  r'Center of the circle:\s*\((-?\d+\.?\d*),\s*(-?\d+\.?\d*)\)'
        match = re.search(pattern, content)
        
        if match:
            p1 = (float(match.group(1)), float(match.group(2)))
            p2 = (float(match.group(3)), float(match.group(4)))
            center = (float(match.group(5)), float(match.group(6)))
            return p1, p2, center
        else:
            raise ValueError("Coordinates not found in the file.")

def calculate_radius(center, point_on_circle):
    x1, y1 = center
    x2, y2 = point_on_circle
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def plot_circle(center, radius, p1, p2):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the circle
    circle = plt.Circle(center, radius, color='blue', fill=False, linestyle='--')
    ax.add_artist(circle)
    
    # Plot the center
    ax.plot(center[0], center[1], 'go', label='Center of the Circle')
    ax.annotate(f'Center: {center}', xy=center, xytext=(center[0] + 1, center[1] + 1),
                arrowprops=dict(facecolor='black', shrink=0.05))
    
    # Plot points on the circle
    ax.plot(p1[0], p1[1], 'ro', label='Point 1')
    ax.plot(p2[0], p2[1], 'ro', label='Point 2')
    ax.annotate(f'Point 1: {p1}', xy=p1, xytext=(p1[0] + 1, p1[1] + 1),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate(f'Point 2: {p2}', xy=p2, xytext=(p2[0] + 1, p2[1] + 1),
                arrowprops=dict(facecolor='black', shrink=0.05))
    
    # Draw the line segment between Point 1 and Point 2
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', label='Line Segment between Points')
    
    # Set the limits of the plot
    ax.set_xlim(min(center[0], p1[0], p2[0]) - radius - 1, max(center[0], p1[0], p2[0]) + radius + 1)
    ax.set_ylim(min(center[1], p1[1], p2[1]) - radius - 1, max(center[1], p1[1], p2[1]) + radius + 1)
    
    # Set equal scaling
    ax.set_aspect('equal', 'box')
    
    # Add grid, legend, and title
    plt.grid(True)
    plt.legend()
    plt.title('Circle Plot with Points and Line Segment')
    
    # Show the plot
    plt.show()

def main():
    filename = '/home/sruthibijili/Desktop/assign3/codes/circle_data.txt'
    try:
        p1, p2, center = read_coordinates_from_file(filename)
        radius = calculate_radius(center, p2)
        
        # Print the coordinates and radius
        print(f'Point 1: {p1}')
        print(f'Point 2: {p2}')
        print(f'Center of the Circle: {center}')
        print(f'The radius of the circle is approximately {radius:.2f}')
        
        # Plot the circle with the line segment
        plot_circle(center, radius, p1, p2)
        
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()

