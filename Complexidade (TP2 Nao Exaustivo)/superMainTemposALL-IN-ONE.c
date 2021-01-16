#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

#define NMAX 200
#define NMIN 5
#define TIPO 3
#define PMAX 49
#define PMIN 25

void calcExaustiva(int * array, long int comprimento);
void calcOtimizada(int * array, long int comprimento);

int main() {
    int * array = NULL;
    long int comprimento[] = {10, 100,500, 1000, 2000, 4000, 8000,10000,20000,40000,80000,100000,200000,400000,800000,1000000,2000000,4000000,8000000,10000000,50000000,100000000,500000000, 1000000000};
    int rand_tipo, rand_perc, rand_n, rand_bin;
    int iComp, tamanhoComp, i, meioArray;

    tamanhoComp = sizeof(comprimento)/sizeof(comprimento[0]);
    srand(time(NULL));

    for (iComp = 0; iComp < tamanhoComp; iComp++) {

        array = (int *) malloc(sizeof(int)*comprimento[iComp]);
        if (array == NULL) {
            printf("Erro no Malloc \n");
            perror("");
            exit(0);
        }

        rand_perc = -1;
        rand_n = -1;
        rand_tipo = rand()%(TIPO+1);
        if (rand_tipo == 1) {
            for (i=0; i < comprimento[iComp]; i++) { /* stdin */
                array[i] = rand()%NMAX;
            }
        }else {
            if (rand_tipo == 0 || rand_tipo == 3) {
                rand_perc = (rand() % (PMAX - PMIN + 1)) + PMIN;

                rand_bin = rand() %2;
                if (rand_bin == 0) {
                    rand_n = (rand() % (NMIN - 2 + 1)) + 2;
                } else {
                    rand_n = 2;
                }

                meioArray = floor(((double) comprimento[iComp]) * (((double) rand_perc) / 100.0));
                for (i = 0; i < meioArray; i++) { /* stdin */
                    array[i] = rand() % NMAX;
                }
                for (i = meioArray; i < comprimento[iComp]; i++) { /* stdin */
                    array[i] = rand() % rand_n;
                }
                rand_tipo = 3;
            }
            else {
                rand_perc = (rand() % (PMAX - PMIN + 1)) + PMIN;

                meioArray = floor(((double) comprimento[iComp]) * (((double) rand_perc) / 100.0));
                for (i = 0; i < meioArray; i++) { /* stdin */
                    array[i] = rand() % NMAX;
                }
                rand_n = rand() % NMAX;
                for (i = meioArray; i < comprimento[iComp]; i++) { /* stdin */
                    array[i] = rand_n;
                }
                rand_n = 1;
            }
        }

        printf("***** Tipos do Random dos Numeros ['1'-> Normal (0 a 255), '2'-> Semelhante ao '3', mas Especial(%%) <=> Quantidade de N-PseudoConstante no Array , '3'-> no array, %d%% a %d%% (Normal: 0 a %d) e %d%% a %d%% (0 a N, N-Max: %d)] *****\n>>> Tipo: %d ||| (Se Tipo '1' -> Ignora (-1) // Se Tipo '2' ou '3' -> Ver:) Normal: %d%%, Especial: %d%%, N.Max.: %d\n", PMIN, PMAX, NMAX, 100 - PMAX, 100 - PMIN, NMIN, rand_tipo, rand_perc, (rand_perc==-1) ? (-1) : (100 - rand_perc), rand_n);

        calcOtimizada(array, comprimento[iComp]);
        if (comprimento[iComp] <= (long int) 1000000)   // 1 MILHAO
            calcExaustiva(array, comprimento[iComp]);
        printf("\n");

        free(array);
        array = NULL;
    }

    return 0;
}

void calcOtimizada(int * array, long int comprimento) {
    int nBits;
    int i, j, n;
    int my_shift;
    struct timespec inicio;
    struct timespec final;
    double tempo_gasto;

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

    printf("FUNCAO OTIMIZADA: N.: %ld | Tempo de Execucao (ms): %f | Resultado: ", comprimento, tempo_gasto); /* Print do Tempo*/

    if ( j >= (int) ( ((floor((double) comprimento/2.0))) + 1)) {
        printf("%d\n", n);
    } else {
        printf("Sem elemento.\n");
    }
}

void calcExaustiva(int * array, long int comprimento) {
    int i, j;
    int n, contadorMaior, contadorTemp = 0;
    struct timespec inicio;
    struct timespec final;
    double tempo_gasto;

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

    printf("FUNCAO EXAUSTIVA: N.: %ld | Tempo de Execucao (ms): %f | Resultado: ", comprimento, tempo_gasto); /* Print do Tempo*/

    if ( contadorMaior >= (int) ( ((floor((double) comprimento/2.0))) + 1)) {
        printf("%d\n", n);
    } else {
        printf("Sem elemento.\n");
    }
}

