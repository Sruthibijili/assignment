import matplotlib.pyplot as plt
import re

def read_points_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Regular expression to extract points
        point_pattern = re.compile(r'Point \d: \(([^,]+), ([^)]+)\)')
        matches = point_pattern.findall(content)
        # Convert matches to list of tuples directly
        return [(float(x), float(y)) for x, y in matches]

def plot_points_and_line(points):
    if not points:
        print("No points to plot.")
        return
    
    # Unpack points
    x_values, y_values = zip(*points)
    
    # Plot points
    plt.scatter(x_values, y_values, color='red', label='Points')
    
    # Plot line between points
    plt.plot(x_values, y_values, color='blue', linestyle='-', linewidth=2, label='Line between points')
    
    # Annotate points with their coordinates
    # Use zip and list comprehensions to add annotations
    annotations = [plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=12, ha='right') for x, y in points]

    # Plot formatting
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points and Line Between Them')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    filename = 'data.txt'
    points = read_points_from_file(filename)
    plot_points_and_line(points)

if __name__ == '__main__':
    main()

