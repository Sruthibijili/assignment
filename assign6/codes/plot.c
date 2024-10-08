#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function declarations
double **createMat(int m, int n);
void printMat(double **p, int m, int n);
double **Matunit(double **a, int m);

int main() {
    // Angles in degrees
    double angles[3] = {90, 60, 30};
    double direction_cosines[3];

    // Calculate direction cosines
    for (int i = 0; i < 3; i++) {
        direction_cosines[i] = cos(angles[i] * M_PI / 180.0); // Convert degrees to radians
    }

    // Create a matrix to hold direction cosines
    double **direction_matrix = createMat(3, 1);
    for (int i = 0; i < 3; i++) {
        direction_matrix[i][0] = direction_cosines[i];
    }

    // Output to console
    printf("Direction Cosines:\n");
    printMat(direction_matrix, 3, 1);

    // Save to file
    FILE *fp = fopen("data.txt", "w");
    if (fp != NULL) {
        fprintf(fp, "Direction Cosines:\n");
        for (int i = 0; i < 3; i++) {
            fprintf(fp, "%lf\n", direction_matrix[i][0]);
        }
        fclose(fp);
        printf("Data saved to data.txt\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    // Free allocated memory
    for (int i = 0; i < 3; i++) {
        free(direction_matrix[i]);
    }
    free(direction_matrix);

    return 0;
}

// Function to create a matrix
double **createMat(int m, int n) {
    double **a;
    a = (double **)malloc(m * sizeof(*a));
    for (int i = 0; i < m; i++)
        a[i] = (double *)malloc(n * sizeof(*a[i]));
    return a;
}

// Function to print a matrix
void printMat(double **p, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            printf("%lf ", p[i][j]);
        printf("\n");
    }
}

