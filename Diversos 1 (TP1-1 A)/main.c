#include <stdio.h>
#include <stdlib.h>

int calcIndice(int i, int j, int col);

int main() {
    int linhas;
    int colunas;
    int inicio2e3Q;         /* O Meio das Colunas */
    int inicio4e3Q;         /* O Meio das Linhas */
    int * matriz = NULL;
    int * matrizTrocada = NULL;
    int temp, iLinha, jColuna, i, j;
    double temp2;


    fscanf(stdin, "%d %d", &linhas, &colunas);
    matriz = (int *) malloc(sizeof(int)*linhas*colunas);
    matrizTrocada = (int *) malloc(sizeof(int)*linhas*colunas);
    if (matriz == NULL || matrizTrocada == NULL) {
        printf("Erro no Malloc \n");
        perror("");
        exit(0);
    }
    for (iLinha = 0 ; iLinha < linhas; iLinha++ ) {
        for (jColuna = 0 ; jColuna < colunas; jColuna++ ) {
            fscanf(stdin, "%d", &temp);
            matriz[calcIndice(iLinha, jColuna, colunas)] = temp;
        }
    }

    temp2 = ( (float) colunas)/2.0;
    inicio2e3Q = (int) temp2;
    temp2 = ( (float) linhas)/2.0;
    inicio4e3Q = (int) temp2;
    inicio2e3Q = colunas - inicio2e3Q;
    inicio4e3Q = linhas - inicio4e3Q;


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

        for (i = 0; i < linhas; i++) {         /* Temp */
            for (j = 0; j < colunas; j++) {
                matriz[calcIndice(i, j, colunas)] = matrizTrocada[calcIndice(i, j, colunas)];
            }
        }

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
    

    /* fprintf(stdout, "%d %d\n", linhas, colunas); */
    for (iLinha = 0 ; iLinha < linhas; iLinha++ ) {
        for (jColuna = 0 ; jColuna < colunas; jColuna++ ) {
            temp = matrizTrocada[calcIndice(iLinha, jColuna, colunas)];
            printf("%d", temp);
            if ( (jColuna + 1) < colunas )
                printf(" ");
        }
        if ( (iLinha + 1) < linhas )
            printf("\n");
    }
    printf("\n");
    /* printf("\nFIM\n"); */
    return 0;
}

int calcIndice(int i, int j, int col) {
    return (i * col + j);
}

