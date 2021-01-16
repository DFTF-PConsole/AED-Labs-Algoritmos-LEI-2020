#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define MY_STDIN "my_stdin2.txt"
#define MY_STDOUT "my_stdout.txt"

int calcIndice(int i, int j, int col);

int main() {
    int linhas;
    int colunas;
    int inicio2e3Q;         /* O Meio das Colunas */
    int inicio4e3Q;         // O Meio das Linhas
    int * matriz = NULL;
    int * matrizTrocada = NULL;
    int temp, iLinha, jColuna, i, j;
    FILE * fpIn;
    FILE * fpOut;

    printf("inicio\n");
    fpIn = fopen(MY_STDIN, "r");
    fpOut = fopen(MY_STDOUT, "w");

    if ( fpIn == NULL || fpOut == NULL) {
        printf("Erro no fopen - %d \n", errno);
        perror("");
        exit(0);
    }


    fscanf(fpIn, "%d %d", &linhas, &colunas);
    printf("Linhas: %d ; Colunas: %d\n", linhas, colunas);
    matriz = (int *) malloc(sizeof(int)*linhas*colunas);
    matrizTrocada = (int *) malloc(sizeof(int)*linhas*colunas);
    if (matriz == NULL || matrizTrocada == NULL) {
        printf("Erro no Malloc \n");
        perror("");
        exit(0);
    }

    for (iLinha = 0 ; iLinha < linhas; iLinha++ ) {
        for (jColuna = 0 ; jColuna < colunas; jColuna++ ) {
            fscanf(fpIn, "%d", &temp);
            matriz[calcIndice(iLinha, jColuna, colunas)] = temp;
        }
    }

    inicio2e3Q = (int) ( (float) colunas)/2.0;
    inicio4e3Q = (int) ( (float) linhas)/2.0;       // porque raio, inicio4e3Q = linhas - ((int) ( (float) linhas)/2.0), da errado!!!??? solucao:
    inicio2e3Q = colunas - inicio2e3Q;
    inicio4e3Q = linhas - inicio4e3Q;
    printf("Meio Linhas: %d e meio colunas: %d\n", inicio4e3Q, inicio2e3Q);

    for (iLinha =  0, i = inicio4e3Q ; i < linhas; iLinha++ , i++) {    //Linhas
        for (j = 0; j < colunas; j++) {
            matrizTrocada[calcIndice(iLinha, j, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    for (i = 0 ; i < inicio4e3Q; iLinha++ , i++) {  // Linhas Part 2
        for (j = 0; j < colunas; j++) {
            matrizTrocada[calcIndice(iLinha, j, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    for (i = 0 ; i < linhas; i++) {         //Temp
        for (j = 0; j < colunas; j++) {
            matriz[calcIndice(i, j, colunas)] = matrizTrocada[calcIndice(i, j, colunas)];
        }
    }

    for (jColuna =  0, j = inicio2e3Q ; j < colunas; jColuna++ , j++) {    // Colunas
        for (i = 0; i < linhas; i++) {
            matrizTrocada[calcIndice(i, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    for ( j = 0 ; j < inicio2e3Q; jColuna++ , j++) {    // Colunas Part 2
        for (i = 0; i < linhas; i++) {
            matrizTrocada[calcIndice(i, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    /*
    for (iLinha =  0, i = inicio4e3Q ; i < linhas; iLinha++ , i++) {         // Troca: (original) 3 -> 1 (final)
        for (jColuna = 0 , j = inicio2e3Q; j < colunas; jColuna++ , j++) {
            matrizTrocada[calcIndice(iLinha, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    for (iLinha =  0, i = inicio4e3Q ; i < linhas; iLinha++ , i++) {         // Troca: 4 -> 2
        for (jColuna = inicio2e3Q , j = 0; jColuna < colunas; jColuna++ , j++) {
            matrizTrocada[calcIndice(iLinha, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    for (iLinha =  inicio4e3Q, i = 0 ; iLinha < linhas; iLinha++ , i++) {         // Troca: 1 -> 3
        for (jColuna = inicio2e3Q , j = 0; jColuna < colunas; jColuna++ , j++) {
            matrizTrocada[calcIndice(iLinha, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }

    for (iLinha =  inicio4e3Q, i = 0 ; iLinha  < linhas; iLinha++ , i++) {         // Troca: 2 -> 4
        for (jColuna = 0 , j = inicio2e3Q; j < colunas; jColuna++ , j++) {
            matrizTrocada[calcIndice(iLinha, jColuna, colunas)] = matriz[calcIndice(i, j, colunas)];
        }
    }
    */


    for (iLinha = 0 ; iLinha < linhas; iLinha++ ) {
        for (jColuna = 0 ; jColuna < colunas; jColuna++ ) {
            temp = matrizTrocada[calcIndice(iLinha, jColuna, colunas)];
            fprintf(fpOut, "%d ", temp);
        }
        fprintf(fpOut, "\n");
    }

    fclose(fpIn);
    fclose(fpOut);
    printf("Fim \n");

    return 0;
}

int calcIndice(int i, int j, int col) {
    return (i * col + j);
}


/* ******************** OUTROS ****************** */
switch (isLinhasImpar) {
case 1:
switch (isColunasImpar) {
case 1: /* Linhas Impar & Colunas Impar */

break;
case 0: /* Linhas Impar & Colunas Par */
break;
}
break;
case 0:
switch (isColunasImpar) {
case 1: /* Linhas Par & Colunas Impar */
break;
case 0: /* Linhas Par & Colunas Par */
break;
}
break;
}

for (iOriginal = 0, iFinal = meioLinhas; iFinal < nLinhas; iOriginal++, iFinal++) {    /* Linhas */
for (jOriginal = 0; jOriginal < nColunas; jOriginal++) {
matrizFinal[calcIndice(iOriginal, jOriginal, nColunas)] = matrizOriginal[calcIndice(iFinal, jOriginal, nColunas)];
}
}

for (iFinal = 0; iFinal < meioLinhas; iOriginal++, iFinal++) {  /* Linhas Part 2 */
for (jOriginal = 0; jOriginal < nColunas; jOriginal++) {
matrizFinal[calcIndice(iOriginal, jOriginal, nColunas)] = matrizOriginal[calcIndice(iFinal, jOriginal, nColunas)];
}
}

for (iFinal = 0; iFinal < nLinhas; iFinal++) {         /* Temp */
for (jFinal = 0; jFinal < nColunas; jFinal++) {
matrizOriginal[calcIndice(iFinal, jFinal, nColunas)] = matrizFinal[calcIndice(iFinal, jFinal, nColunas)];
}
}

for (jOriginal = 0, j = meioColunas; j < nColunas; jOriginal++, j++) {    /* Colunas */
for (i = 0; i < nLinhas; i++) {
matrizFinal[calcIndice(i, jOriginal, nColunas)] = matrizOriginal[calcIndice(i, j, nColunas)];
}
}

for (j = 0; j < meioColunas; jOriginal++, j++) {    /* Colunas Part 2 */
for (i = 0; i < nLinhas; i++) {
matrizFinal[calcIndice(i, jOriginal, nColunas)] = matrizOriginal[calcIndice(i, j, nColunas)];
}
}
