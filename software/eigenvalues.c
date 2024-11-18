#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void qr_decompose(double **A, double **Q, double **R, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Q[i][j] = A[i][j];
            R[i][j] = 0;
        }
    }

    for (int j = 0; j < n; j++) {
        for (int k = 0; k < j; k++) {
            double dot_product = 0;
            for (int i = 0; i < n; i++) {
                dot_product += Q[i][k] * Q[i][j];
            }
            for (int i = 0; i < n; i++) {
                Q[i][j] -= dot_product * Q[i][k];
            }
        }

        double norm = 0;
        for (int i = 0; i < n; i++) {
            norm += Q[i][j] * Q[i][j];
        }
        norm = sqrt(norm);
        for (int i = 0; i < n; i++) {
            Q[i][j] /= norm;
        }

        for (int k = 0; k < n; k++) {
            R[k][j] = 0;
            for (int i = 0; i < n; i++) {
                R[k][j] += Q[i][k] * A[i][j];
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
        qr_decompose(A, Q, R, n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    A[i][j] += R[i][k] * Q[k][j];
                }
            }
        }

        double off_diag_sum = 0;
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
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

    printf("Enter matrix elements:\n");
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


