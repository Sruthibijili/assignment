#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to perform Householder reflection
void householder_reflection(double **A, double **Q, double **R, int n) {
    for (int j = 0; j < n; j++) {
        // Compute the Householder vector v
        double norm = 0;
        for (int i = j; i < n; i++) {
            norm += A[i][j] * A[i][j];
        }
        norm = sqrt(norm);
        
        double alpha = (A[j][j] > 0) ? -norm : norm;
        double r = sqrt(0.5 * (norm * norm - A[j][j] * alpha));
        
        // Set the first element of v to be the difference
        double v_j = A[j][j] - alpha;
        A[j][j] = v_j;
        
        // Apply the reflection to matrix A
        for (int i = j + 1; i < n; i++) {
            A[i][j] /= v_j;
        }
        
        for (int i = j; i < n; i++) {
            for (int k = j; k < n; k++) {
                Q[i][k] -= 2 * A[i][j] * A[k][j];
            }
        }
    }
}

// Function to perform QR iteration using Householder reflections
void qr_iteration(double **A, int n) {
    double **Q = (double **)malloc(n * sizeof(double *));
    double **R = (double **)malloc(n * sizeof(double *));
    
    for (int i = 0; i < n; i++) {
        Q[i] = (double *)malloc(n * sizeof(double));
        R[i] = (double *)malloc(n * sizeof(double));
    }

    // Iterate until matrix A converges to a diagonal form
    for (int iter = 0; iter < 1000; iter++) {
        // Perform QR decomposition using Householder reflections
        householder_reflection(A, Q, R, n);
        
        // Multiply Q and R to get A = Q * R
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    A[i][j] += R[i][k] * Q[k][j];
                }
            }
        }
        
        // Check if off-diagonal elements are sufficiently small (convergence criterion)
        double off_diag_sum = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                off_diag_sum += A[i][j] * A[i][j];
            }
        }
        if (off_diag_sum < 1e-6) break;  // Convergence threshold
    }

    // Output the eigenvalues (diagonal elements of A)
    printf("Eigenvalues:\n");
    for (int i = 0; i < n; i++) {
        printf("%f ", A[i][i]);
    }
    printf("\n");

    // Free memory for Q and R
    for (int i = 0; i < n; i++) {
        free(Q[i]);
        free(R[i]);
    }
    free(Q);
    free(R);
}

int main() {
    int n;
    printf("Enter matrix size (n x n): ");
    scanf("%d", &n);

    // Allocate memory for matrix A
    double **A = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        A[i] = (double *)malloc(n * sizeof(double));
    }

    // Input matrix elements
    printf("Enter matrix elements (row by row):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &A[i][j]);
        }
    }

    // Perform QR iteration to find eigenvalues
    qr_iteration(A, n);

    // Free memory for matrix A
    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);

    return 0;
}

