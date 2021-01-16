#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

int main() {
    int * array = NULL;
    int nBits;
    int comprimento = 0;
    int i, j, n;
    int my_shift;
    struct timespec inicio;
    struct timespec final;
    double tempo_gasto;
    int my_rand;

    fscanf(stdin, "%d %d", &comprimento, &my_rand);
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

    srand(time(0));
    i=0;
    while (i < comprimento) { /* stdin */
        array[i] = rand()%my_rand;
        i++;
    }

    clock_gettime(CLOCK_REALTIME, &inicio); /* Contador = Tempo Inicial */

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

    clock_gettime(CLOCK_REALTIME, &final); /* Contador = Tempo Final */
    tempo_gasto = (double) (final.tv_sec - inicio.tv_sec)*1000.0 + (double) (final.tv_nsec - inicio.tv_nsec)/1000000.0;    /* Tempo em ms */

    printf("*****\nTempo de Execucao (ms): %f\n*****\n", tempo_gasto); /* Print do Tempo*/

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
 *  0 0 0 0 0 0 0 0 = N
 *  0 0 0 0 0 0 1 1 = 3
 *  0 0 0 0 0 0 1 1 = OR
 *  0 0 0 0 0 0 1 1 = 3
 *  0 0 0 0 0 0 1 1 = 3
 *  Maioria 1's ->>>
 *  0 0 0 0 0 0 1 0 = 2
 *  NOTA: Quando contados a maioria de 1's em cada coluna (do byte), o numero gerado pode nao ser maioritario, sendo necessario verificar no array
 */