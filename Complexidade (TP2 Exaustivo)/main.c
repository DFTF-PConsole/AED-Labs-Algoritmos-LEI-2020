#include <stdio.h>
#include <math.h>

int main() {
    int array[1024]; /* Pensar Numa Solucao Array Dinamica - Sugestao: Usar um Ciclo -> 1. iteracao usar malloc, 2ou+ usar realloc para aumentar o tamanho (50 em 50 bytes * typeof) */
    int comprimento;
    int i, j;
    int n, contadorMaior, contadorTemp = 0;
    char termina;

    i=0;
    comprimento = 0;
    termina = ' ';
    while (termina != '\n') { /* stdin */
            fscanf(stdin, "%d%c", &array[i], &termina);
            i++;
            comprimento++;
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

    return 0;
}

/*  PROBLEMA 1 - Parte A (Modo Exaustivo) O(N^2) -> ao Quadrado
 *  Dado um Lista de Numeros Dizer Se um Numero e Maioritario ou Nao e Qual E
 *
 *  Ex.: INPUT: 1 2 2 4 5 2 2 -> OUTPUT: 2
 *  Ex.: INPUT: 1 2 2 4 5 2 -> OUTPUT: Sem elemento.
 *  Ex.: INPUT: 1 2 2 4 5 3 6 -> OUTPUT: Sem elemento.
 */