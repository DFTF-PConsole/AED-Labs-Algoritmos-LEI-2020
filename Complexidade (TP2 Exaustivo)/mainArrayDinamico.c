#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define TAMANHO 50  /* <<<NOVO>>> - ArrayDinamico | Tamanho Inicial do Array Dinamico, Posteriormente sera aumentado tamanho = tamanho*2 */

int main() {
    int * array = NULL; /* <<<NOVO>>> - ArrayDinamico | Pensar Numa Solucao Array Dinamica - Sugestao: Usar um Ciclo -> 1. iteracao usar malloc, 2ou+ usar realloc para aumentar o tamanho (50 em 50 bytes * typeof) */
    int comprimento;
    int i, j;
    int n, contadorMaior, contadorTemp = 0;
    char termina;
    int * ptr = NULL; /* <<<NOVO>>> - ArrayDinamico */
    int fator, tamanhoBlocoArray; /* <<<NOVO>>> - ArrayDinamico */

    tamanhoBlocoArray = TAMANHO;    /* <<<NOVO>>> - ArrayDinamico */
    array = (int *) malloc(sizeof(int)*tamanhoBlocoArray);  /* <<<NOVO>>> - ArrayDinamico */
    if (array == NULL) {    /* <<<NOVO>>> (e dentro do if) - ArrayDinamico */
        printf("Erro no Malloc\n");
        perror("");
        exit(0);
    }

    i=0;
    comprimento = 0;
    termina = ' ';
    fator = tamanhoBlocoArray;  /* <<<NOVO>>> - ArrayDinamico */
    while (termina != '\n') { /* stdin */
        fscanf(stdin, "%d%c", &array[i], &termina);
        i++;
        comprimento++;
        if (comprimento>=fator) {   /* <<<NOVO>>> (e dentro do if) - ArrayDinamico */
            tamanhoBlocoArray = tamanhoBlocoArray*2;
            fator = fator + tamanhoBlocoArray;
            ptr = realloc(array, sizeof(int)*tamanhoBlocoArray);
            if (ptr == NULL) {
                printf("Erro no Realloc\n");
                perror("");
                free(array);
                exit(0);
            }
            array = ptr;
        }
    }

    for (i=0, contadorMaior = 0, n=0; i<comprimento; i++) {
        for (j=0, contadorTemp=0; j<comprimento; j++) {
            if (array[i] == array[j]) {
                contadorTemp++;
            }
        }
        if (contadorTemp > contadorMaior) {
            n = array[i];
            contadorMaior = contadorTemp;
        }
    }

    if ( contadorMaior >= (int) ( ((floor((double) comprimento/2.0))) + 1)) {
        printf("%d\n", n);
    } else {
        printf("Sem elemento.\n");
    }

    free(array);
    return 0;
}

/*  PROBLEMA 1 - Parte A (Modo Exaustivo) O(N^2) -> ao Quadrado
 *  Dado um Lista de Numeros Dizer Se um Numero e Maioritario ou Nao e Qual E
 *
 *  Ex.: INPUT: 1 2 2 4 5 2 2 -> OUTPUT: 2
 *  Ex.: INPUT: 1 2 2 4 5 2 -> OUTPUT: Sem elemento.
 *  Ex.: INPUT: 1 2 2 4 5 3 6 -> OUTPUT: Sem elemento.
 */