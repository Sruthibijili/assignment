#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void householder_reflection(double **A, double **Q, double **R, int n) {
    for (int j = 0; j < n; j++) {
        double norm = 0;
        for (int i = j; i < n; i++) {
            norm += A[i][j] * A[i][j];
        }
        norm = sqrt(norm);
        
        double alpha = (A[j][j] > 0) ? -norm : norm;
        double r = sqrt(0.5 * (norm * norm - A[j][j] * alpha));
        
        double v_j = A[j][j] - alpha;
        A[j][j] = v_j;
        
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

void qr_iteration(double **A, int n) {
    double **Q = (double **)malloc(n * sizeof(double *));
    double **R = (double **)malloc(n * sizeof(double *));
    
    for (int i = 0; i < n; i++) {
        Q[i] = (double *)malloc(n * sizeof(double));
        R[i] = (double *)malloc(n * sizeof(double));
    }

    for (int iter = 0; iter < 1000; iter++) {
        householder_reflection(A, Q, R, n);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    A[i][j] += R[i][k] * Q[k][j];
                }
            }
        }
        
        double off_diag_sum = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                off_diag_sum += A[i][j] * A[i][j];
            }
        }
        if (off_diag_sum < 1e-6) break;  
    }

    printf("Eigenvalues:\n");
    for (int i = 0; i < n; i++) {
        printf("%f ", A[i][i]);
    }
    printf("\n");

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

    double **A = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        A[i] = (double *)malloc(n * sizeof(double));
    }

    printf("Enter matrix elements (row by row):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &A[i][j]);
        }
    }

    qr_iteration(A, n);

    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);

    return 0;
}

