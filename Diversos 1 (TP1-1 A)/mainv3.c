#include <stdio.h>
#include <stdlib.h>

long int calcIndice(long int i, long int j, long int col);

int main() {
    long int linhas;
    long int colunas;
    long int inicio2e3Q;         /* O Meio das Colunas */
    long int inicio4e3Q;         /* O Meio das Linhas */
    long int * matriz = NULL;
    long int * matrizTrocada = NULL;
    long int temp, iLinha, jColuna, i, j;
    double temp2;


    fscanf(stdin, "%ld %ld", &linhas, &colunas);
    matriz = (long int *) malloc(sizeof(long int)*linhas*colunas);
    matrizTrocada = (long int *) malloc(sizeof(long int)*linhas*colunas);
    if (matriz == NULL || matrizTrocada == NULL) {
        printf("Erro no Malloc \n");
        perror("");
        exit(0);
    }
    for (iLinha = 0 ; iLinha < linhas; iLinha++ ) {
        for (jColuna = 0 ; jColuna < colunas; jColuna++ ) {
            fscanf(stdin, "%ld", &temp);
            matriz[calcIndice(iLinha, jColuna, colunas)] = temp;
        }
    }

    temp2 = ( (float) colunas)/2.0;
    inicio2e3Q = (long int) temp2;
    temp2 = ( (float) linhas)/2.0;
    inicio4e3Q = (long int) temp2;
    inicio2e3Q = colunas - inicio2e3Q;
    inicio4e3Q = linhas - inicio4e3Q;

    if (linhas > 1) {
        for (iLinha = 0, i = inicio4e3Q; i < linhas; iLinha++, i++) {    /* Linhas */
            for (j = 0; j < colunas; j++) {
                matrizTrocada[calcIndice(iLinha, j, colunas)] = matriz[calcIndice(i, j, colunas)];
            }
        }

        for (i = 0; i < inicio4e3Q; iLinha++, i++) {  /* Linhas Part 2 */
            for (j = 0; j < colunas; j++) {
                matrizTrocada[calcIndice(iLinha, j, colunas)] = matriz[calcIndice(i, j, colunas)];
            }
        }
    } else {
        for (i = 0 ; i < linhas; i++) {
            for (j = 0; j < colunas; j++) {
                matrizTrocada[calcIndice(i, j, colunas)] = matriz[calcIndice(i, j, colunas)];
            }
        }
    }

    for (i = 0 ; i < linhas; i++) {         /* Temp */
        for (j = 0; j < colunas; j++) {
            matriz[calcIndice(i, j, colunas)] = matrizTrocada[calcIndice(i, j, colunas)];
        }
    }

    if (colunas > 1) {
        for (jColuna = 0, j = inicio2e3Q; j < colunas; jColuna++, j++) {    /* Colunas */
            for (i = 0; i < linhas; i++) {
                matrizTrocada[calcIndice(i, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
            }
        }

        for (j = 0; j < inicio2e3Q; jColuna++, j++) {    /* Colunas Part 2 */
            for (i = 0; i < linhas; i++) {
                matrizTrocada[calcIndice(i, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
            }
        }
    }

    /* fprintf(stdout, "%d %d\n", linhas, colunas); */
    for (iLinha = 0 ; iLinha < linhas; iLinha++ ) {
        for (jColuna = 0 ; jColuna < colunas; jColuna++ ) {
            temp = matrizTrocada[calcIndice(iLinha, jColuna, colunas)];
            fprintf(stdout, "%ld", temp);
            if ( (jColuna + 1) < colunas )
                fprintf(stdout, " ");
        }
        if ( (iLinha + 1) < linhas )
            fprintf(stdout, "\n");
    }
    printf("\n");
    /* printf("\nFIM\n"); */
    return 0;
}

long int calcIndice(long int i, long int j, long int col) {
    return (i * col + j);
}

