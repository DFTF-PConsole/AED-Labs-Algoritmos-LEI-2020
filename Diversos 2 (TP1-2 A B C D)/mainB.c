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
 *    Ficha 1.1 | B - Ex B
 *    FCTUC - DEI/LEI - AED
 *    Coimbra, 18 de fevereiro de 2020
 *************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int main() {

    int i, j, n, soma, valor, terminar;
    int * array;

    while (1) {
        terminar = 0;
        fscanf(stdin, "%d %d", &n, &valor);
        printf("\nn: %d - valor: %d\n", n, valor); /* temp - eliminar na submissao*/
        if (n == 0 && valor == 0)
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
            soma = 0;
            for (j = i; (j < n) && (terminar == 0); j++) {
                soma = soma + array[j];
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




