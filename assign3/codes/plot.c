include <stdio.h>

int main() {
    // Define the endpoints of the diameter
    int x1 = -6, y1 = 3;
    int x2 = 6, y2 = 4;

    // Calculate the midpoint (center of the circle)
    double centerX = (x1 + x2) / 2.0;
    double centerY = (y1 + y2) / 2.0;

    // Open a file for writing
    FILE *file = fopen("circle_data.txt", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the points and the center to the file
    fprintf(file, "Point 1: (%d, %d)\n", x1, y1);
    fprintf(file, "Point 2: (%d, %d)\n", x2, y2);
    fprintf(file, "Center of the circle: (%.2f, %.2f)\n", centerX, centerY);

    // Close the file
    fclose(file);

    printf("Data has been written to circle_data.txt\n");

    return 0;
