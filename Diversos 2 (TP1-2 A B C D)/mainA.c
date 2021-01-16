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
 *    Ficha 1.1 | B - Ex A
 *    FCTUC - DEI/LEI - AED
 *    Coimbra, 18 de fevereiro de 2020
 *************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int main() {

    int i, j, z, n, soma, valor, terminar;
    int * array;

    while (1) {
        terminar = 0;
        fscanf(stdin, "%d %d", &n, &valor);
        printf("\nn: %d - valor: %d\n", n, valor); /* temp - eliminar na submissao*/
        if (n == 0 && valor == 0)   /* Nota: para detetar os  ultimos 2 '0's, tem que haver \n, pelo menos no IDE*/
            break;

        array = (int *) malloc(sizeof(int) * n);
        if (array == NULL) {
            printf("Erro no Malloc \n");
            perror("");
            exit(1);
        }

        for (i = 0; i < n; i++) {
            fscanf(stdin, "%d", &j);
            array[i] = j;
        }

        for (i = 0; (i < n) && (terminar == 0); i++) {
            for (j = i; (j < n) && (terminar == 0); j++) {
                soma = 0;
                for (z = i; z <= j; z++) {
                    soma = soma + array[z];
                }
                if (soma == valor) {
                    printf("Subsequencia na posicao %d\n", i+1);
                    free(array);
                    terminar = 1;
                }
            }
        }
        if (terminar == 0) {
            printf("Subsequencia nao existe\n");
            free(array);
        }
    }


    return 0;
}




