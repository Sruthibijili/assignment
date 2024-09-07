#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Define the points
    int x1 = -5, y1 = 4;
    int x2 = -1, y2 = 6;

    // Calculate the midpoint
    int x_mid = (x1 + x2) / 2;
    int y_mid = (y1 + y2) / 2;

    // Write points and midpoint to the file
    fprintf(file, "Point 1: (%d, %d)\n", x1, y1);
    fprintf(file, "Point 2: (%d, %d)\n", x2, y2);
    fprintf(file, "Midpoint: (%d, %d)\n", x_mid, y_mid);

    // Close the file
    fclose(file);

    printf("Points and midpoint have been written to data.txt\n");

    return 0;
}

