# v1: Ordenacao para "arrays alvo" -> Com QuickSort (A1) para array "incial", com InsertionSort para array com os elementos finais
# *** VERSAO RELATORIO *** | Tabela 2 e 3


# #### BIBLIOTECAS ####
import sys
import time
import msvcrt
from io import StringIO


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
    textos_relatorio = ["A", "B", "C", "D"]

    for n_texto in textos_relatorio:
        print("# # # # # # TEXTO " + n_texto + " # # # # # #")
        nome_fich = "./StdinsCalculaTempos/StdinTexto" + n_texto + "RelatorioF4.txt"
        array_palavras = []  # [omg, xd, a, ahah] | Input "palavra + ID"
        array_count_global = []  # [3, 1, 10, 2] ou [[3, 0], [1, 1], [10, 2], [2, 3]] [Count, Indice]
        array_count_utilizadores = []  # [2, 1, 5, 2] > [[Count, Indice], ...]
        acumula_global = 0
        acumula_utilizadores = 0

        while msvcrt.kbhit():  # Clean stdin Windows
            msvcrt.getch()

        my_file = open(nome_fich, "r")
        my_stdin = my_file.read()
        my_file.close()
        sys.stdin = StringIO(my_stdin)

        if sys.stdin.readline() == CMD_IN_PALAVRAS:
            array_palavras, array_count_global, array_count_utilizadores = input_palavras(array_palavras, array_count_global,
                                                                                          array_count_utilizadores)
        else:
            sys.exit("Erro - Sem Comando Incial: " + CMD_IN_PALAVRAS)
        print("+++++++++")
        print(array_palavras)
        print("+++++++++")
        for i in range(20):
            print("###### Tentativa " + str(i+1) + " ######")
            temp_array_count_global = []
            temp_array_count_utilizadores = []
            for j in range(len(array_palavras)):
                temp_array_count_global.append(array_count_global[j])
                temp_array_count_utilizadores.append(array_count_utilizadores[j])
            tempo_global, tempo_utilizadores = input_cmd(array_palavras, temp_array_count_global, temp_array_count_utilizadores)
            acumula_global = acumula_global + tempo_global
            acumula_utilizadores = acumula_utilizadores + tempo_utilizadores
            print("##############\n")

        print("#########################################")
        acumula_global = (acumula_global / 20.0) * 1000
        acumula_utilizadores = (acumula_utilizadores / 20.0) * 1000
        print("***** Tempo MEDIO em MS - PESQUISA GLOBAL = " + str(acumula_global) + " *****")
        print("***** Tempo MEDIO em MS - PESQUISA UTILIZADORES = " + str(acumula_utilizadores) + " *****")
        print("#########################################\n\n")

    return 0


def input_palavras(array_palavras, array_count_global, array_count_utilizadores):
    # ### FUNCAO ### Le e manipula o texto do stdin ate CMD_IN_FIM
    array_ids_utilizadores = []              # [[109, 114], [109], [455,677,232,124,345], [098,345]] , IDs - Diferentes
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
    tempo_global = tempo_utilizadores = 0

    start_cmd = time.time()
    array_count_global = ordenacao(array_count_global)
    end_cmd = time.time()
    tempo_global = end_cmd - start_cmd
    print("*Tempo em MS - CMD-PesquisaGlobal = " + str(tempo_global * 1000) + " ||| Start Vs End: " + str(start_cmd) +
          "|" + str(end_cmd) + " *")

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

    start_cmd = time.time()
    array_count_utilizadores = ordenacao(array_count_utilizadores)
    end_cmd = time.time()
    tempo_utilizadores = end_cmd - start_cmd
    print("*Tempo em MS - CMD-PesquisaUtilizadores = " + str(tempo_utilizadores * 1000) + " ||| Start Vs End: " +
          str(start_cmd) + "|" + str(end_cmd) + " *")
    print(array_count_utilizadores)
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

    return tempo_global, tempo_utilizadores


def insertion_sort(array, indice_baixo, indice_alto):
    for i in range(indice_baixo, indice_alto + 1):
        temp = array[i]         # Elemento a comparar
        j = i - 1                # Começa com o elemento a baixo do temp
        while j >= indice_baixo and temp[0] < array[j][0]:  # ORDEM CRESCENTE, enquanto temp MENOR array[j] -> os elementos sobem um degrau
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp              # temp fica abaixo dos demais que subiram 1 degrau
    return array


def quick_sort(array, indice_baixo, indice_alto):
    # ### FUNCAO ### Quick Sort para Inteiros
    if PARAGEM_CORTE > (indice_alto - indice_baixo):        # Array < 30 elementos -> Insertion
        array = insertion_sort(array, indice_baixo, indice_alto)
    else:
        indice_meio = int((indice_baixo + indice_alto) / 2)
        if array[indice_alto][0] < array[indice_baixo][0]:    # Mediana
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

        pivot = array[indice_meio][0]         # Nomeia PIVOT
        temp = array[indice_meio]                 # Troca pivot  com (ultimo_elemento - 1)
        array[indice_meio] = array[indice_alto - 1]
        array[indice_alto - 1] = temp

        ptr_baixo = indice_baixo
        ptr_alto = indice_alto - 1
        while True:   # Percorre parte-do-array com ponteiros, a semelhanca nos slides 72 a 80 - Cap 6A ORD COM CHAVES
            ptr_alto = ptr_alto - 1
            ptr_baixo = ptr_baixo + 1
            while array[ptr_alto][0] > pivot:
                ptr_alto = ptr_alto - 1
            while array[ptr_baixo][0] < pivot:
                ptr_baixo = ptr_baixo + 1
            if ptr_baixo < ptr_alto:     # Troca
                temp = array[ptr_alto]
                array[ptr_alto] = array[ptr_baixo]
                array[ptr_baixo] = temp
            else:
                break

        temp = array[indice_meio]    # Troca NOVAMENTE pivot  no (ultimo_elemento - 1) com ptr_baixo =aprox= meio (backup)
        array[indice_meio] = array[indice_alto - 1]
        array[indice_alto - 1] = temp

        array = quick_sort(array, indice_baixo, ptr_baixo - 1)    # Parte o array em dois
        array = quick_sort(array, ptr_baixo + 1, indice_alto)

    return array


def ordenacao(array):
    # ### FUNCAO ### *Abstracao* -> Chama a funcao de ordenamento
    array = quick_sort(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    # ### START ###
    main()
