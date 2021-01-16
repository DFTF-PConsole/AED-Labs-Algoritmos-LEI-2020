# v1: Com Insertion Sort dos arrays finais, INPUT-PALAVRAS: SEM ordenacao por insercao e pesquisa binaria no array_palavras e no array auxiliar dos IDs para eficiencia


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
            indice = len(array_palavras) - 1
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


def insertion_sort(array):
    # ### FUNCAO ### Insertion Sort para Inteiros
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp[0] < array[j][0]:   # ORDEM CRESCENTE
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


def ordenacao(array):
    # ### FUNCAO ### *Abstracao* -> Chama a funcao de ordenamento
    array = insertion_sort(array)
    return array


if __name__ == '__main__':
    # ### START ###
    main()
