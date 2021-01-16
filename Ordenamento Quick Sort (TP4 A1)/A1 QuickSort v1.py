# v1: Ordenacao para "arrays alvo" -> Com QuickSort para array "incial", com InsertionSort para array com os elementos finais
# INPUT-PALAVRAS: SEM ordenacao por insercao NEM pesquisa binaria no array_palavras e no array auxiliar dos IDs para eficiencia


# #### BIBLIOTECAS ####
import sys


# #### CONSTANTES ####
CMD_IN_GLOBAL = "PESQ_GLOBAL\n"
CMD_IN_UTILIZADORES = "PESQ_UTILIZADORES\n"
CMD_IN_TERMINADO = "TCHAU\n"
CMD_IN_TERMINADO2 = "TCHAU"
CMD_IN_PALAVRAS = "PALAVRAS\n"
CMD_IN_FIM = "FIM.\n"
CMD_OUT_GUARDADO = "GUARDADAS"
PARAGEM_CORTE = 30


# #### FUNCOES ####
def main():
    # ### FUNCAO ### Funcao Principal
    array_palavras = []                     # [omg, xd, a, ahah] | Input "palavra + ID"
    array_count_global = []                 # [3, 1, 10, 2] ou [[3, 0], [1, 1], [10, 2], [2, 3]] [Count, Indice]
    array_count_utilizadores = []           # [2, 1, 5, 2] > [[Count, Indice], ...]
    # array_utilizadores = []               # [[109, 114], [109], [455,677,232,124,345], [098,345]] , IDs - Diferentes

    if sys.stdin.readline() == CMD_IN_PALAVRAS:
        array_palavras, array_count_global, array_count_utilizadores = input_palavras(array_palavras, array_count_global, array_count_utilizadores)
    else:
        sys.exit("Erro - Sem Comando Incial: " + CMD_IN_PALAVRAS)

    input_cmd(array_palavras, array_count_global, array_count_utilizadores)

    return 0


def input_palavras(array_palavras, array_count_global, array_count_utilizadores):
    # ### FUNCAO ### Le e manipula o texto do stdin ate CMD_IN_FIM
    array_ids_utilizadores = []                                                                                         # [[109, 114], [109], [455,677,232,124,345], [098,345]] , IDs - Diferentes
    for linha in sys.stdin:
        if linha == "\n" or linha == "":
            sys.exit("Erro - Sem Texto para input")
        if linha == CMD_IN_FIM:
            break
        palavras = linha.split(" ")
        palavras[0] = palavras[0].upper()
        palavras[1] = palavras[1][:-1]
        if palavras[0] in array_palavras:
            indice = array_palavras.index(palavras[0])
            array_count_global[indice][0] += 1
            if not int(palavras[1]) in array_ids_utilizadores[indice]:
                array_ids_utilizadores[indice].append(int(palavras[1]))
                array_count_utilizadores[indice][0] += 1
        else:
            array_palavras.append(palavras[0])
            indice = len(array_palavras)-1
            array_ids_utilizadores.append([int(palavras[1])])
            array_count_global.append([1, indice])
            array_count_utilizadores.append([1, indice])
    print(CMD_OUT_GUARDADO)
    return array_palavras, array_count_global, array_count_utilizadores


def input_cmd(array_palavras, array_count_global, array_count_utilizadores):
    # ### FUNCAO ### Le, executa e escreve no stdout os comandos no stdin, ate CMD_IN_TERMINADO
    for linha in sys.stdin:
        if linha == CMD_IN_TERMINADO2:
            break
        elif linha == CMD_IN_TERMINADO:
            break
        elif linha == "":
            break
        elif linha == CMD_IN_GLOBAL:
            array_count_global = ordenacao(array_count_global)
            string = ""
            valor = array_count_global[-1][0]
            start = len(array_palavras) - 1
            for i in range(len(array_palavras)-1, -1, -1):
                if valor == array_count_global[i][0]:
                    start = i
                else:
                    break
            alvo = []
            for i in range(start, len(array_palavras)):
                indice = array_count_global[i][1]
                alvo.append(array_palavras[indice])
            alvo.sort()
            for i in range(len(alvo)):
                string = string + str(alvo[i]) + " "
            print(string[:-1])
        elif linha == CMD_IN_UTILIZADORES:
            array_count_utilizadores = ordenacao(array_count_utilizadores)
            string = ""
            valor = array_count_utilizadores[-1][0]
            start = len(array_palavras)-1
            for i in range(len(array_palavras)-1, -1, -1):
                if valor == array_count_utilizadores[i][0]:
                    start = i
                else:
                    break
            alvo = []
            for i in range(start, len(array_palavras)):
                indice = array_count_utilizadores[i][1]
                alvo.append(array_palavras[indice])
            alvo.sort()
            for i in range(len(alvo)):
                string = string + str(alvo[i]) + " "
            print(string[:-1])
        else:
            sys.exit("Erro - Interpretacao dos comandos pos-palavras")
    return 0


def insertion_sort(array, indice_baixo, indice_alto):
    for i in range(indice_baixo, indice_alto + 1):
        temp = array[i]                                                                                                 # Elemento a comparar
        j = i - 1                                                                                                       # Começa com o elemento a baixo do temp
        while j >= indice_baixo and temp[0] < array[j][0]:                                                              # ORDEM CRESCENTE, enquanto temp MENOR array[j] ->> os elementos sobem um degrau
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp                                                                                             # temp fica abaixo dos demais que subiram 1 degrau
    return array


def quick_sort(array, indice_baixo, indice_alto):
    # ### FUNCAO ### Quick Sort para Inteiros
    if PARAGEM_CORTE > (indice_alto - indice_baixo):                                                                    # Array < 30 elementos -> Insertion
        array = insertion_sort(array, indice_baixo, indice_alto)
    else:
        indice_meio = int((indice_baixo + indice_alto) / 2)
        if array[indice_alto][0] < array[indice_baixo][0]:                                                              # Mediana
            temp = array[indice_alto]
            array[indice_alto] = array[indice_baixo]
            array[indice_baixo] = temp
        if array[indice_meio][0] < array[indice_baixo][0]:
            temp = array[indice_meio]
            array[indice_meio] = array[indice_baixo]
            array[indice_baixo] = temp
        if array[indice_meio][0] < array[indice_alto][0]:
            temp = array[indice_meio]
            array[indice_meio] = array[indice_alto]
            array[indice_alto] = temp

        pivot = array[indice_meio][0]                                                                                   # Nomeia PIVOT
        temp = array[indice_meio]                                                                                       # Troca pivot  com (ultimo_elemento - 1)
        array[indice_meio] = array[indice_alto - 1]
        array[indice_alto - 1] = temp

        ptr_baixo = indice_baixo
        ptr_alto = indice_alto - 1
        while True:                                                                                                     # Percorre parte-do-array com ponteiros, a semelhanca nos slides 72 a 80 - Cap 6A ORD COM CHAVES
            ptr_alto = ptr_alto - 1
            ptr_baixo = ptr_baixo + 1
            while array[ptr_alto][0] > pivot:
                ptr_alto = ptr_alto - 1
            while array[ptr_baixo][0] < pivot:
                ptr_baixo = ptr_baixo + 1
            if ptr_baixo < ptr_alto:                                                                                    # Troca
                temp = array[ptr_alto]
                array[ptr_alto] = array[ptr_baixo]
                array[ptr_baixo] = temp
            else:
                break

        temp = array[indice_meio]                                                                                       # Troca NOVAMENTE pivot  no (ultimo_elemento - 1) com ptr_baixo =aprox= meio (backup)
        array[indice_meio] = array[indice_alto - 1]
        array[indice_alto - 1] = temp

        array = quick_sort(array, indice_baixo, ptr_baixo - 1)                                                          # Parte o array em dois
        array = quick_sort(array, ptr_baixo + 1, indice_alto)

    return array


def ordenacao(array):
    # ### FUNCAO ### *Abstracao* -> Chama a funcao de ordenamento
    array = quick_sort(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    # ### START ###
    main()
