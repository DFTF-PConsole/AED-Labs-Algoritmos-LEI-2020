# v2 - Melhoramentos: Retirei "in" em "x in array"; implementei pesquisa binaria e ordenaçao por inserçao; print_array; etc.
# 2 ARRAYS: 1 para palavras, 1 para guardar o numero em que ocorre
# *** VERSAO RELATORIO ***


# #### BIBLIOTECAS ####
import sys
import time
import msvcrt
from io import StringIO


# #### CONSTANTES ####
CMD_IN_LINHAS = "LINHAS"
CMD_OUT_NULO = "-1"
CMD_IN_ASSOC = "ASSOC"
CMD_OUT_NAOENCONTRADA = "NAO ENCONTRADA."
CMD_OUT_ENCONTRADA = "ENCONTRADA."
CMD_IN_TERMINADO = "TCHAU\n"
CMD_IN_TERMINADO2 = "TCHAU"
CMD_IN_TEXTO = "TEXTO\n"
CMD_IN_FIM = "FIM.\n"
CMD_OUT_GUARDADO = "GUARDADO."


# #### VARS GLOBAIS ####
acumula_linhas = 0
acumula_assoc = 0


# #### FUNCOES ####
def main():
    # ### FUNCAO ### Funcao Principal
    textos_relatorio = ["A", "B", "C", "D"]
    global acumula_linhas
    global acumula_assoc
    for n_texto in textos_relatorio:
        print("# # # # # # TEXTO " + n_texto + " # # # # # #")
        acumula_texto = 0
        acumula_linhas = 0
        acumula_assoc = 0
        for i in range(20):
            array_palavras = []  # Varias Palavras
            array_ocorrencias = [[]]
            while msvcrt.kbhit():   # Clean stdin Windows
                msvcrt.getch()
            if n_texto == "A" or n_texto == "D":
                nome_fich = "./StdinsCalculaTempos/StdinTexto" + n_texto + "RelatorioN" + str(i) + ".txt"
            else:
                nome_fich = "./StdinsCalculaTempos/StdinTexto" + n_texto + "RelatorioN" + str(0) + ".txt"
            print("########" + nome_fich + "########")
            my_file = open(nome_fich, "r")
            my_stdin = my_file.read()
            my_file.close()
            sys.stdin = StringIO(my_stdin)
            if sys.stdin.readline() == CMD_IN_TEXTO:
                start_texto = time.time()
                array_palavras, array_ocorrencias = input_texto(array_palavras, array_ocorrencias)
                end_texto = time.time()
                tempo_texto = end_texto - start_texto
            else:
                sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)
            input_cmd(array_palavras, array_ocorrencias)
            acumula_texto = acumula_texto + tempo_texto
            print("#########################################\n")
        acumula_texto = acumula_texto / 20.0
        acumula_linhas = acumula_linhas / 20.0
        acumula_assoc = acumula_assoc / 20.0
        print("* * * * * Tempo Medio em Segundos Input TEXTO = " + str(acumula_texto) + " * * * * *")
        print("* * * * * Tempo Medio em Segundos Input CMDs - LINHAS = " + str(acumula_linhas) + " * * * * *")
        print("* * * * * Tempo Medio em Segundos Input CMDs - ASSOC = " + str(acumula_assoc) + " * * * * *")
        print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n\n")
    return 0


def input_texto(array_palavras, array_ocorrencias):
    # ### FUNCAO ### Le e manipula o texto do stdin ate CMD_IN_FIM
    count = 0
    conta_palavras_diferente = 0
    conta_palavras = 0
    for linha in sys.stdin:
        if count == 0 and linha == "":
            sys.exit("Erro - Sem Texto para input")

        if linha == CMD_IN_FIM:
            break
        palavra = ""
        for ch in linha:
            if ch == '\n':
                if len(palavra) > 0:
                    conta_palavras = conta_palavras + 1
                    palavra = palavra.lower()
                    indice_palavra = pesquisa_binaria(array_palavras, palavra)
                    if not (indice_palavra == -1):
                        if not (count == array_ocorrencias[indice_palavra][-1]):
                            array_ocorrencias[indice_palavra].append(count)
                    else:
                        array_palavras, array_ocorrencias = inserir_array(array_palavras, palavra, array_ocorrencias, count)
                        conta_palavras_diferente = conta_palavras_diferente + 1
                palavra = ""
            elif ch == ' ' or ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')':
                if len(palavra) > 0:
                    conta_palavras = conta_palavras + 1
                    palavra = palavra.lower()
                    indice_palavra = pesquisa_binaria(array_palavras, palavra)
                    if not (indice_palavra == -1):
                        if not (count == array_ocorrencias[indice_palavra][-1]):
                            array_ocorrencias[indice_palavra].append(count)
                    else:
                        array_palavras, array_ocorrencias = inserir_array(array_palavras, palavra, array_ocorrencias, count)
                        conta_palavras_diferente = conta_palavras_diferente + 1
                indice_palavra = pesquisa_binaria(array_palavras, ch)
                if not (indice_palavra == -1):
                    if not (count == array_ocorrencias[indice_palavra][-1]):
                        array_ocorrencias[indice_palavra].append(count)
                else:
                    array_palavras, array_ocorrencias = inserir_array(array_palavras, ch, array_ocorrencias, count)
                palavra = ""
            else:
                palavra = palavra + ch
        count += 1
    print(CMD_OUT_GUARDADO)
    print("* * * * * Palavras Total no Texto = " + str(conta_palavras) + " * * * * *")
    print("* * * * * Palavras Diferentes no Texto = " + str(conta_palavras_diferente) + " * * * * *")
    return array_palavras, array_ocorrencias


def input_cmd(array_palavras, array_ocorrencias):
    # ### FUNCAO ### Le, executa e escreve no stdout os comandos no stdin, ate CMD_IN_TERMINADO
    fator_assoc = 0
    fator_linhas = 0
    inicio_assoc = 0
    inicio_linhas = 0
    global acumula_assoc
    global acumula_linhas
    for linha in sys.stdin:
        if linha == CMD_IN_TERMINADO2:
            break
        elif linha == CMD_IN_TERMINADO:
            break
        elif linha == "":
            break
        elif (CMD_IN_LINHAS in linha) and (linha.index(CMD_IN_LINHAS) == 0):
            if fator_assoc == 1:
                acumula_assoc = acumula_assoc + (time.time() - inicio_assoc)
                fator_assoc = -1
            if fator_linhas == 0:
                inicio_linhas = time.time()
                fator_linhas = 1
            palavra = linha[len(CMD_IN_LINHAS)+1:len(linha)-1]
            palavra = palavra.lower()

            indice_palavra = pesquisa_binaria(array_palavras, palavra)
            if not (indice_palavra == -1):
                print(print_array(array_ocorrencias[indice_palavra]))
            else:
                print(CMD_OUT_NULO)
        elif (CMD_IN_ASSOC in linha) and (linha.index(CMD_IN_ASSOC) == 0):
            if fator_linhas == 1:
                acumula_linhas = acumula_linhas + (time.time() - inicio_linhas)
                fator_linhas = -1
            if fator_assoc == 0:
                inicio_assoc = time.time()
                fator_assoc = 1
            palavras = linha.split(' ')
            palavras[2] = (palavras[2])[:len(palavras[2])-1]
            palavras[1] = palavras[1].lower()

            indice_palavra = pesquisa_binaria(array_palavras, palavras[1])
            if not (indice_palavra == -1):
                if not (pesquisa_binaria(array_ocorrencias[indice_palavra], int(palavras[2])) == -1):   # Confirmar Alteracao
                    print(CMD_OUT_ENCONTRADA)
                else:
                    print(CMD_OUT_NAOENCONTRADA)
            else:
                print(CMD_OUT_NAOENCONTRADA)
        else:
            sys.exit("Erro - Interpretacao dos comandos pos-texto")
    if fator_linhas == 1:
        acumula_linhas = acumula_linhas + (time.time() - inicio_linhas)
    if fator_assoc == 1:
        acumula_assoc = acumula_assoc + (time.time() - inicio_assoc)
    return 0


def pesquisa_binaria(array, valor):
    # ### FUNCAO ### Pesquisa Binaria Classica num Array/Lista, input array e valor, return indice ou -1 se nao existir
    inicio = 0
    fim = len(array)-1
    if fim == -1:
        return -1
    while inicio <= fim:
        meio = inicio + (fim - inicio) // 2    # Divisao Real, Arredonda para baixo
        if array[meio] == valor:       # Valor esta no meio?
            return meio
        elif array[meio] < valor:        # Se valor e maior que o meio, ignora metade inferior
            inicio = meio + 1
        else:                         # Se for menor que o meio, ignora metade superior
            fim = meio - 1
    return -1                             # Nao existe


def print_array(array):
    # ### FUNCAO ### Transforma os dados num array numa string com espacos
    string = ""
    for num in array:
        string = string + " " + str(num)
    return string[1:]


def inserir_array(array_palavras, palavra, array_ocorrencias, count):
    # ### FUNCAO ### Inserir palavra e n-linha pela primeira vez nos arrays, ordenacao por insercao
    index = len(array_palavras)
    if index == 0:   # Se primeira palavra no array
        array_palavras.append(palavra)
        array_ocorrencias[0].append(count)
        return array_palavras, array_ocorrencias
    for i in range(len(array_palavras)):    # Procura pela posicao
        if i == index:
            break
        if array_palavras[i] > palavra:   # Ordenacao por insercao
            index = i
            break
    array_palavras = array_palavras[:index] + [palavra] + array_palavras[index:]    # Inserir
    array_ocorrencias = array_ocorrencias[:index] + [[count]] + array_ocorrencias[index:]
    return array_palavras, array_ocorrencias


if __name__ == '__main__':
    # ### START ###
    main()
