# Gera Stdins dos diversos textos com reaproveitamente do codigo de A0
# Le Pasta Inputs -> Gera e guarda em Outputs


# #### BIBLIOTECAS ####
import sys
import msvcrt
from io import StringIO
import random


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


# #### FUNCOES ####
def main():
    # ### FUNCAO ### Funcao Principal
    textos_relatorio = ["A", "B", "C", "D"]
    for n_texto in textos_relatorio:
        print("###### TEXTO " + n_texto + " ######")
        array_palavras = []  # Varias Palavras
        array_ocorrencias = [[]]  # Ocorrencias/N linhas - String -> Ex.: "1 2 3"
        while msvcrt.kbhit():  # Clean stdin Windows
            msvcrt.getch()
        nome_fich = "./Inputs/StdinTexto" + n_texto + ".txt"
        my_file = open(nome_fich, "r")
        my_stdin = my_file.read()
        my_file.close()
        sys.stdin = StringIO(my_stdin)
        if sys.stdin.readline() == CMD_IN_TEXTO:
            array_palavras, array_ocorrencias = input_texto(array_palavras, array_ocorrencias)
        else:
            sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)
        if n_texto == "A":
            for i in range(20):
                nome_fich = "./Outputs/StdinTexto" + n_texto + "RelatorioN" + str(i) + ".txt"
                my_file = open(nome_fich, "w")
                for line in my_stdin.splitlines():
                    if line == "FIM.":
                        my_file.write(line + "\n")
                        break
                    my_file.write(line + "\n")
                for j in range(50):
                    n = random.randint(0, len(array_palavras)-1)
                    my_file.write("LINHAS " + array_palavras[n] + "\n")
                fator = 0
                for j in range(50):
                    n = random.randint(0, len(array_palavras)-1)
                    if fator == 0:  # facil
                        fator = 1
                        ocorrencia = array_ocorrencias[n][(len(array_ocorrencias[n])-1)//2]
                    elif fator == 1: # dificil
                        fator = 2
                        ocorrencia = array_ocorrencias[n][0]
                    else:   # nao existe
                        fator = 0
                        ocorrencia = array_ocorrencias[n][-1] + 1
                    my_file.write("ASSOC " + array_palavras[n] + " " + str(ocorrencia) + "\n")
                my_file.write("TCHAU\n\n\n")
                my_file.close()
        elif n_texto == "B" or n_texto == "C":
            nome_fich = "./Outputs/StdinTexto" + n_texto + "RelatorioN" + str(0) + ".txt"
            my_file = open(nome_fich, "w")
            for line in my_stdin.splitlines():
                if line == "FIM.":
                    my_file.write(line + "\n")
                    break
                my_file.write(line + "\n")
            my_file.write("TCHAU\n\n\n")
            my_file.close()
        elif n_texto == "D":
            for i in range(20):
                nome_fich = "./Outputs/StdinTexto" + n_texto + "RelatorioN" + str(i) + ".txt"
                my_file = open(nome_fich, "w")
                for line in my_stdin.splitlines():
                    if line == "FIM.":
                        my_file.write(line + "\n")
                        break
                    my_file.write(line + "\n")
                lista_palavras = []
                for j in range(10):
                    n = random.randint(0, len(array_palavras)-1)
                    while array_palavras[n] in lista_palavras:
                        n = random.randint(0, len(array_palavras)-1)
                    lista_palavras.append(array_palavras[n])
                for j in range(50):
                    n = random.randint(0, len(lista_palavras)-1)
                    my_file.write("LINHAS " + lista_palavras[n] + "\n")
                my_file.write("TCHAU\n\n\n")
                my_file.close()
        print("######################################")
    return 0


def input_texto(array_palavras, array_ocorrencias):
    # ### FUNCAO ### Le e manipula o texto do stdin ate CMD_IN_FIM
    count = 0
    for linha in sys.stdin:
        if count == 0 and linha == "":
            sys.exit("Erro - Sem Texto para input")
        if linha == CMD_IN_FIM:
            break
        palavra = ""
        for ch in linha:
            if ch == '\n':
                if len(palavra) > 0:
                    palavra = palavra.lower()
                    indice_palavra = pesquisa_binaria(array_palavras, palavra)
                    if not (indice_palavra == -1):
                        if not (count == array_ocorrencias[indice_palavra][-1]):
                            array_ocorrencias[indice_palavra].append(count)
                    else:
                        array_palavras, array_ocorrencias = inserir_array(array_palavras, palavra, array_ocorrencias, count)
                palavra = ""
            elif ch == ' ' or ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')':
                if len(palavra) > 0:
                    palavra = palavra.lower()
                    indice_palavra = pesquisa_binaria(array_palavras, palavra)
                    if not (indice_palavra == -1):
                        if not (count == array_ocorrencias[indice_palavra][-1]):
                            array_ocorrencias[indice_palavra].append(count)
                    else:
                        array_palavras, array_ocorrencias = inserir_array(array_palavras, palavra, array_ocorrencias, count)
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
    return array_palavras, array_ocorrencias


def pesquisa_binaria(array, valor):
    # ### FUNCAO ### Pesquisa Binaria Classica num Array/Lista, input array e valor, return indice ou -1 se nao existir
    inicio = 0
    fim = len(array)-1
    if fim == -1:
        return -1
    while inicio <= fim:
        meio = inicio + (fim - inicio) // 2                                                                             # Divisao Real, Arredonda para baixo
        if array[meio] == valor:                                                                                        # Valor esta no meio?
            return meio
        elif array[meio] < valor:                                                                                       # Se valor e maior que o meio, ignora metade inferior
            inicio = meio + 1
        else:                                                                                                           # Se for menor que o meio, ignora metade superior
            fim = meio - 1
    return -1                                                                                                           # Nao existe


def inserir_array(array_palavras, palavra, array_ocorrencias, count):
    # ### FUNCAO ### Inserir palavra e n-linha pela primeira vez nos arrays, ordenacao por insercao
    index = len(array_palavras)
    if index == 0:                                                                                                      # Se primeira palavra no array
        array_palavras.append(palavra)
        array_ocorrencias[0].append(count)
        return array_palavras, array_ocorrencias
    for i in range(len(array_palavras)):                                                                                # Procura pela posicao
        if i == index:
            break
        if array_palavras[i] > palavra:                                                                                 # Ordenacao por insercao
            index = i
            break
    array_palavras = array_palavras[:index] + [palavra] + array_palavras[index:]                                        # Inserir
    array_ocorrencias = array_ocorrencias[:index] + [[count]] + array_ocorrencias[index:]
    return array_palavras, array_ocorrencias


if __name__ == '__main__':
    # ### START ###
    main()
