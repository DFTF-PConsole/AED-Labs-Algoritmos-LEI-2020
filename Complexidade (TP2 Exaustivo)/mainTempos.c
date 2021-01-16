#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>


int main() {
    int * array = NULL;
    int comprimento = 0;
    int i, j;
    int n, contadorMaior, contadorTemp = 0;
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

    for (i=0, contadorMaior = 0, n=0; i<comprimento && ( contadorMaior < (int) ( ((floor((double) comprimento/2.0))) + 1)); i++) {
        for (j=i, contadorTemp=0; j<comprimento && ( contadorTemp < (int) ( ((floor((double) comprimento/2.0))) + 1)); j++) {
            if (array[i] == array[j]) {
                contadorTemp++;
            }
        }
        if (contadorTemp > contadorMaior) {
            n = array[i];
            contadorMaior = contadorTemp;
        }
    }

    clock_gettime(CLOCK_REALTIME, &final); /* Contador = Tempo Final */
    tempo_gasto = (double) (final.tv_sec - inicio.tv_sec)*1000.0 + (double) (final.tv_nsec - inicio.tv_nsec)/1000000.0;    /* Tempo em ms */

    printf("*****\nTempo de Execucao (ms): %f\n*****\n", tempo_gasto); /* Print do Tempo*/

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