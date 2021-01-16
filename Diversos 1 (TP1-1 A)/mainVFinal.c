/* *****************************************************************************
 * "YOU MAY THINK THAT THIS FUNCTION IS OBSOLETE AND DOESNT SEEM TO DO ANYTHING
 * AND YOU WOULD BE CORRECT BUT WHEN WE REMOVE THIS FUNCTION FOR SOME REASON
 * THE WHOLE PROGRAM CRASHES AND WE CANT FIGURE OUT WHY SO HERE IT WILL STAY"
 *                                                        - Fernando Pessoa
 *    Autores:
 *        > Dario Felix (N.2018275530)
 *
 *    Agradecimentos:
 *        > Google
 *        > Stackoverflow
 *        > IDEs
 *        > Take Away do Pingo Doce
 *        > Cafe
 *
 *    Ficha 1 - Ex A
 *    FCTUC - DEI/LEI - AED
 *    Coimbra, 15 de fevereiro de 2020
 *************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

/* 1Q | 2Q
 * 4Q | 3Q
 */

long int calcIndice(long int i_linha, long int j_coluna, long int n_colunas);

int main() {
    long int nLinhas;
    long int nColunas;
    long int meioColunas, meioColunasDepois;
    long int meioLinhas, meioLinhasDepois;
    long int * matrizOriginal = NULL;
    long int * matrizFinal = NULL;
    long int tempLongInt, iOriginal, jOriginal, iFinal, jFinal;
    double tempDouble;
    long int isLinhasImpar, isColunasImpar;

    fscanf(stdin, "%ld %ld", &nLinhas, &nColunas);

    matrizOriginal = (long int *) malloc(sizeof(long int)*nLinhas*nColunas);
    matrizFinal = (long int *) malloc(sizeof(long int)*nLinhas*nColunas);
    if (matrizOriginal == NULL || matrizFinal == NULL) {
        printf("Erro no Malloc \n");
        perror("");
        exit(0);
    }

    for (iOriginal = 0 ; iOriginal < nLinhas; iOriginal++ ) { /* stdin */
        for (jOriginal = 0 ; jOriginal < nColunas; jOriginal++ ) {
            fscanf(stdin, "%ld", &tempLongInt);
            matrizOriginal[calcIndice(iOriginal, jOriginal, nColunas)] = tempLongInt;
            matrizFinal[calcIndice(iOriginal, jOriginal, nColunas)] = tempLongInt; /* Temp, usado especialmente em impares */
        }
    }

    tempDouble = ( (double) nColunas)/2.0;
    meioColunas = (long int) tempDouble;
    tempDouble = ( (double) nLinhas)/2.0;
    meioLinhas = (long int) tempDouble;
    isLinhasImpar = nLinhas % 2;
    isColunasImpar = nColunas % 2;
    meioLinhasDepois = meioLinhas + isLinhasImpar;
    meioColunasDepois = meioColunas + isColunasImpar;


    for (iFinal =  0, iOriginal = meioLinhasDepois ; iOriginal < nLinhas; iOriginal++ , iFinal++) { /* Troca: (original) 3 -> 1 (final) */
        for (jFinal = 0 , jOriginal = meioColunasDepois; jOriginal < nColunas; jOriginal++ , jFinal++) {
            matrizFinal[calcIndice(iFinal, jFinal, nColunas)] = matrizOriginal[calcIndice(iOriginal, jOriginal, nColunas)];
        }
    }

    for (iFinal = 0, iOriginal = meioLinhasDepois ; iOriginal < nLinhas; iOriginal++ , iFinal++) { /* Troca: (original) 4 -> 2 (final) */
        for (jFinal = meioColunasDepois , jOriginal = 0; jFinal < nColunas; jOriginal++ , jFinal++) {
            matrizFinal[calcIndice(iFinal, jFinal, nColunas)] = matrizOriginal[calcIndice(iOriginal, jOriginal, nColunas)];
        }
    }

    for (iFinal =  meioLinhasDepois, iOriginal = 0 ; iFinal < nLinhas; iOriginal++ , iFinal++) { /* Troca: (original) 1 -> 3 (final) */
        for (jFinal = meioColunasDepois , jOriginal = 0; jFinal < nColunas; jOriginal++ , jFinal++) {
            matrizFinal[calcIndice(iFinal, jFinal, nColunas)] = matrizOriginal[calcIndice(iOriginal, jOriginal, nColunas)];
        }
    }

    for (iFinal =  meioLinhasDepois, iOriginal = 0 ; iFinal  < nLinhas; iOriginal++ , iFinal++) { /* Troca: (original) 2 -> 4 (final) */
        for (jFinal = 0 , jOriginal = meioColunasDepois; jOriginal < nColunas; jOriginal++ , jFinal++) {
            matrizFinal[calcIndice(iFinal, jFinal, nColunas)] = matrizOriginal[calcIndice(iOriginal, jOriginal, nColunas)];
        }
    }


    for (iFinal = 0 ; iFinal < nLinhas; iFinal++ ) { /* Print -> stdout */
        for (jFinal = 0 ; jFinal < nColunas; jFinal++ ) {
            tempLongInt = matrizFinal[calcIndice(iFinal, jFinal, nColunas)];
            printf("%ld", tempLongInt);
            if ( (jFinal + 1) < nColunas )
                printf(" ");
        }
        if ( (iFinal + 1) < nLinhas )
            printf("\n");
    }
    printf("\n");

    free(matrizFinal); /* Limpar Alocacoes Dinamicas */
    free(matrizOriginal);

    return 0;
}

long int calcIndice(long int i_linha, long int j_coluna, long int n_colunas) {
    return (i_linha * n_colunas + j_coluna);
}



