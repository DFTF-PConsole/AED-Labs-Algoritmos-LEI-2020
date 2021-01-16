#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COMINTEXTO "TEXTO\n"
#define COMINFIM "FIM."
#define COMOUTGUARDADO "GUARDADO.\n"
#define COMINLINHAS "LINHAS"
#define COMOUTNULO "-1\n"
#define COMINASSOC "ASSOC"
#define COMOUTNAOENCONTRADA "NAO ENCONTRADA.\n"
#define COMOUTENCONTRADA "ENCONTRADA.\n"
#define COMINTERMINADO "TERMINADO"
#define MAXPALAVRAS 100         /* Conjunto de Palavras */
#define MAXCHAR 30         /* Conjunto de Char por Palavras */

/* MUITO Incompleto, Problemas com o utf-8 >> Solucao: Python */

int main() {
    char comando[25];
    char temp_palavra[MAXCHAR];
    char * conjunto_palavras;
    char * conjunto_nlinhas;
    int i;

    for (i=0; i < 25 ;i++) {
        fscanf(stdin, "%c", &comando[i]);
        if (comando[i] == '\n') {
            comando[i+1] = '\0';
            break;
        }
    }

    if (strcmp(comando, COMINTEXTO) == 0) {

        for (i=0; i < 25 ; i++) {
            fscanf(stdin, "%c", &comando[i]);
            if (comando[i] == '\n') {
                comando[i+1] = '\0';
                break;
            }
        }




    } else {
        printf("Erro Comando - Expetativa: \"%s\" Vs. Realidade: \"%s\" \n", COMINTEXTO, comando);
        exit(1);
    }


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
}

int indice(indice_linhas, indice_colunas, colunas) {
    return indice_linhas * colunas + indice_colunas;
}

/*
 * conjunto_palavras[i][0] <-> conjunto_nlinhas[i][0] | i-> palavra no indice i, inicio da string a 0 -> conjunto de linhas no indice i, inicio da string a 0 (string do tipo: 1 3 5 6)
 * ** Colocar tudo em minusculas **
 */

