# v1: Com Radix Sort LSD (A2) (Lado Direito -> Lado Esquerdo) Atua Sobre Digitos e Nao Bits (Para inteiros) |
# Ex.: 1999 >>> 1 <- 9 <- 9 <- 9
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


# #### FUNCOES ####
def main():
    # ### FUNCAO ### Funcao Principal
    array_palavras = []  # [omg, xd, a, ahah] | Input "palavra + ID"
    array_count_global = []  # [3, 1, 10, 2] ou [[3, 0], [1, 1], [10, 2], [2, 3]] [Count, Indice]
    array_count_utilizadores = []  # [2, 1, 5, 2] > [[Count, Indice], ...]
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
            array_palavras, array_count_global, array_count_utilizadores = input_palavras(array_palavras,
                                                                                          array_count_global,
                                                                                          array_count_utilizadores)
        else:
            sys.exit("Erro - Sem Comando Incial: " + CMD_IN_PALAVRAS)
        print("+++++++++")
        print(array_palavras)
        print("+++++++++")
        for i in range(20):
            print("###### Tentativa " + str(i + 1) + " ######")
            temp_array_count_global = []
            temp_array_count_utilizadores = []
            for j in range(len(array_palavras)):
                temp_array_count_global.append(array_count_global[j])
                temp_array_count_utilizadores.append(array_count_utilizadores[j])
            tempo_global, tempo_utilizadores = input_cmd(array_palavras, temp_array_count_global,
                                                         temp_array_count_utilizadores)
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
    tempo_global = tempo_utilizadores = 0

    start_cmd = time.time()
    array_count_global = ordenacao(array_count_global)
    end_cmd = time.time()
    tempo_global = end_cmd - start_cmd
    print("*Tempo em MS - CMD-PesquisaGlobal = " + str(tempo_global * 1000) + " ||| Start Vs End: " + str(
        start_cmd) + "|" + str(end_cmd) + " *")
    string = ""
    valor = array_count_global[-1][0]
    start = len(array_palavras) - 1
    for i in range(len(array_palavras) - 1, -1, -1):
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
    print("*Tempo em MS - CMD-PesquisaUtilizadores = " + str(tempo_utilizadores * 1000) + " ||| Start Vs End: " + str(
        start_cmd) + "|" + str(end_cmd) + " *")
    string = ""
    valor = array_count_utilizadores[-1][0]
    start = len(array_palavras) - 1
    for i in range(len(array_palavras) - 1, -1, -1):
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


# v1: Com Radix Sort LSD (A2) (Lado Direito -> Lado Esquerdo) Atua Sobre Digitos e Nao Bits (Para inteiros) |
# Ex.: 1999 >>> 1 <- 9 <- 9 <- 9
# *** VERSAO RELATORIO *** | Tabela 2 e 3


def radix_sort(array, tamanho):
    # ### FUNCAO ### Radix Sort para Inteiros

    max_digitos = len(str(max(array[:][0])))            # Numero Maior no Array -> Quantos Digitos?

    array_contador = []                                 # Contar cada digito
    array_semiordenado = []                             # Auxiliar: array -> sort -> array_semiordenado -> copia -> array

    divisor = 1
    for j in range(max_digitos):                        # Passar por todos os digitos do numero
        for i in range(10):
            array_contador.append(0)
        for i in range(tamanho):
            array_semiordenado.append(0)

        for i in range(tamanho):                        # Contar as ocorrencias de cada digito
            digito = int((array[i][0]/divisor) % 10)
            array_contador[digito] = array_contador[digito] + 1

        temp = temp_anterior = 0
        for i in range(1, 10):                          # array_contador[i] -> fica com a posicao onde se colocam os numeros com
                                                                                                # este digito no array_semiordenado
            temp = array_contador[i]
            array_contador[i] = array_contador[i-1] + temp_anterior     # Ver Exemplo/Explicacao nas Notas-iPad
            temp_anterior = temp
        array_contador[0] = 0                           # Digitos com comecam no Indice 0 (e o primeiro)

        for i in range(tamanho):                        # Semi-Ordena com base nos digitos e posicao no array_contador
            digito = int((array[i][0]/divisor) % 10)
            array_semiordenado[array_contador[digito]] = array[i]
            array_contador[digito] = array_contador[digito] + 1

        for i in range(tamanho):                        # COPIA: De 'array_semiordenado' Para 'array'
            array[i] = array_semiordenado[i]

        divisor = divisor * 10                          # *** Prepara a proxima iteracao do ciclo ***
        array_contador = []
        array_semiordenado = []

    return array


def ordenacao(array):
    # ### FUNCAO ### *Abstracao* -> Chama a funcao de ordenamento
    array = radix_sort(array, len(array))
    return array


if __name__ == '__main__':
    # ### START ###
    main()
