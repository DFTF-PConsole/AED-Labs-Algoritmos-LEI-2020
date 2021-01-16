# v1: Com Insertion Sort dos arrays finais (A0) | Especial Relatorio
# *** VERSAO RELATORIO *** | Tabela 1

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


# #### FUNCOES ####
def main():
    # ### FUNCAO ### Funcao Principal
    array_palavras = []                     # [omg, xd, a, ahah] | Input "palavra + ID"
    array_count_global = []                 # [3, 1, 10, 2] ou [[3, 0], [1, 1], [10, 2], [2, 3]] [Count, Indice]
    array_count_utilizadores = []           # [2, 1, 5, 2] > [[Count, Indice], ...]
    array_ids_utilizadores = []             # [[109, 114], [109], [455,677,232,124,345], [098,345]] , IDs - Diferentes
    n_total = 0
    textos_relatorio = ["A", "B", "C", "D"]

    for n_texto in textos_relatorio:
        print("# # # # # # TEXTO " + n_texto + " # # # # # #")
        nome_fich = "./StdinsCalculaTempos/StdinTexto" + n_texto + "RelatorioF4.txt"
        acumula_texto = 0
        n_palavras_distintas = 0
        n_utilizadores_distintos = 0
        n_pares_distintas = 0
        for i in range(20):
            print("###### Tentativa " + str(i+1) + " ######")
            array_palavras = []  # [omg, xd, a, ahah] | Input "palavra + ID"
            array_count_global = []  # [3, 1, 10, 2] ou [[3, 0], [1, 1], [10, 2], [2, 3]] [Count, Indice]
            array_count_utilizadores = []  # [2, 1, 5, 2] > [[Count, Indice], ...]
            array_ids_utilizadores = []  # [[109, 114], [109], [455,677,232,124,345], [098,345]] , IDs - Diferentes
            n_total = 0

            while msvcrt.kbhit():  # Clean stdin Windows
                msvcrt.getch()

            my_file = open(nome_fich, "r")
            my_stdin = my_file.read()
            my_file.close()
            sys.stdin = StringIO(my_stdin)

            if sys.stdin.readline() == CMD_IN_PALAVRAS:
                start_texto = time.time()
                array_palavras, array_count_global, array_count_utilizadores, array_ids_utilizadores, n_total = \
                    input_palavras(array_palavras, array_count_global, array_count_utilizadores, array_ids_utilizadores)
                end_texto = time.time()
                tempo_texto = end_texto - start_texto
                print("*Tempo em MS - Carregamento/Input TEXTO = " + str(tempo_texto * 1000) + " ||| Start Vs End: " +
                      str(start_texto) + "|" + str(end_texto) + " *")
                acumula_texto = acumula_texto + tempo_texto
            else:
                sys.exit("Erro - Sem Comando Incial: " + CMD_IN_PALAVRAS)

        acumula_texto = (acumula_texto / 20.0) * 1000
        print("***** Tempo Medio em MS - Carregamento/Input TEXTO = " + str(acumula_texto) + " *****")
        print("#########################################\n")

        n_palavras_distintas = len(array_palavras)
        n_pares_distintas = 0
        for i in range(len(array_ids_utilizadores)):
            n_pares_distintas = n_pares_distintas + len(array_ids_utilizadores[i])
        array_utilizadores_distintos = []
        for i in range(len(array_ids_utilizadores)):
            for j in range(len(array_ids_utilizadores[i])):
                if not array_ids_utilizadores[i][j] in array_utilizadores_distintos:
                    array_utilizadores_distintos.append(array_ids_utilizadores[i][j])
        n_utilizadores_distintos = len(array_utilizadores_distintos)
        print("\n#########################################")
        print("***** Numero de Palavras Distintas = " + str(n_palavras_distintas) + " *****")
        print(array_palavras)
        print("***** Numero de Utilizadores Distintos = " + str(n_utilizadores_distintos) + " *****")
        print(array_utilizadores_distintos)
        print("***** Numero de Pares Distintos (Palavra-Utilizador) = " + str(n_pares_distintas) + " *****")
        print(array_ids_utilizadores)
        print("***** Numero Total de Palavras/Utilizadores (Entradas) = " + str(n_total) + " *****")
        print("+++++++++")
        input_cmd(array_palavras, array_count_global, array_count_utilizadores)
        print("+++++++++")
        print("#########################################\n\n")

    return 0


def input_palavras(array_palavras, array_count_global, array_count_utilizadores, array_ids_utilizadores):
    # ### FUNCAO ### Le e manipula o texto do stdin ate CMD_IN_FIM
    n_total = 0
    for linha in sys.stdin:
        if linha == "\n" or linha == "":
            sys.exit("Erro - Sem Texto para input")
        if linha == CMD_IN_FIM:
            break
        n_total = n_total + 1
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
    return array_palavras, array_count_global, array_count_utilizadores, array_ids_utilizadores, n_total


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
