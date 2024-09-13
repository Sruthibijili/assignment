#include <stdio.h>
#include <math.h>

int main() {
    // Compute the value of sqrt(21) and k
    double sqrt21 = sqrt(21);       // Compute sqrt(21)
    double k = 3 + 2 * sqrt21;      // Compute k = 3 + 2 * sqrt(21)

    // Define the coordinates of the points
    double x1 = k;
    double y1 = -2;
    double x2 = 3;
    double y2 = -6;

    // Open the file data.txt for writing
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the points to the file
    fprintf(file, "The points are:\n");
    fprintf(file, "Point 1: (%.2f, %.2f)\n", x1, y1);
    fprintf(file, "Point 2: (%.2f, %.2f)\n", x2, y2);

    // Close the file
    fclose(file);

    printf("The points have been written to data.txt\n");

    return 0;
}

