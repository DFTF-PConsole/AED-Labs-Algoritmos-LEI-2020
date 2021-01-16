#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int * array = NULL;
    int comprimento = 0;
    int i, j;
    int n, contadorMaior, contadorTemp = 0;

    fscanf(stdin, "%d", &comprimento);
    if (comprimento <= 0) {
        printf("Erro no Comprimento <= 0 \n");
        exit(0);
    }
    array = (int *) malloc(sizeof(int)*comprimento);
    if (array == NULL) {
        printf("Erro no Malloc \n");
        perror("");
        exit(0);
    }

    i=0;
    while (i < comprimento) { /* stdin */
            fscanf(stdin, "%d", &array[i]);
            i++;
    }

    for (i=0, contadorMaior = 0, n=0; i<comprimento && ( contadorMaior < (int) ( ((floor((double) comprimento/2.0))) + 1)); i++) {
        for (j=0, contadorTemp=0; j<comprimento && ( contadorTemp < (int) ( ((floor((double) comprimento/2.0))) + 1)); j++) {
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

    return 0;
}

/*  PROBLEMA 1 - Parte A (Modo Exaustivo) O(N^2) -> ao Quadrado
 *  Dado um Lista de Numeros Dizer Se um Numero e Maioritario ou Nao e Qual E
 *
 *  Ex.: INPUT: 1 2 2 4 5 2 2 -> OUTPUT: 2
 *  Ex.: INPUT: 1 2 2 4 5 2 -> OUTPUT: Sem elemento.
 *  Ex.: INPUT: 1 2 2 4 5 3 6 -> OUTPUT: Sem elemento.
 */