#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int * array = NULL;    /* Pensar Numa Solucao Array Dinamica - Sugestao: Usar um Ciclo -> 1. iteracao usar malloc, 2ou+ usar realloc para aumentar o tamanho (50 em 50 bytes * typeof) */
    int nBits;
    int comprimento = 0;
    int i, j, n;
    int my_shift;

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

    for (j=0, my_shift = 1, n=0; j<8; j++) {
        for (i=0, nBits=0; i < comprimento && ( nBits < (int) ( ((floor((double) comprimento/2.0))) + 1)) ; i++) {
            if (array[i] & my_shift) {
                nBits++;
            }
        }
        if ( nBits >= (int) ( ((floor((double) comprimento/2.0))) + 1)) {
            n = n | my_shift;
        }
        my_shift = my_shift<<1;
    }

    for (j=0, i=0; i<comprimento ;i++) {
        if (n == array[i])
            j++;
    }
    if ( j >= (int) ( ((floor((double) comprimento/2.0))) + 1)) {
        printf("%d\n", n);
    } else {
        printf("Sem elemento.\n");
    }

    return 0;
}

/*  PROBLEMA 1 - Parte B (Modo NAO Exaustivo) O(k*N + N) = O(N) -> Linearmente
 *  Dado um Lista de Numeros Dizer Se um Numero e Maioritario ou Nao e Qual E
 *
 *  Ex.: INPUT: 1 2 2 4 5 2 2 -> OUTPUT: 2
 *  Ex.: INPUT: 1 2 2 4 5 2 -> OUTPUT: Sem elemento.
 *  Ex.: INPUT: 1 2 2 4 5 3 6 -> OUTPUT: Sem elemento.
 *
 *  Conta-se os Bits da mesma Coluna:
 *  0 0 0 0 0 0 1 0 = 2
 *  0 0 0 0 0 0 1 0 = 2
 *  0 0 0 0 0 0 0 1 = 1
 *  0 0 0 0 1 0 0 0 = 8
 *  0 0 0 0 0 0 1 0 = 2
 *  Maioria 1's ->>>
 *  0 0 0 0 0 0 1 0 = 2
 *  NOTA: Quando contados a maioria de 1's em cada coluna (do byte), o numero gerado pode nao ser maioritario, sendo necessario verificar no array
 */