# v2 - Melhoramentos: Retirei "in" em "x in array"; implementei pesquisa binaria e ordenaçao por inserçao; print_array; etc.
# 2 ARRAYS: 1 para palavras, 1 para guardar o numero em que ocorre


# #### BIBLIOTECAS ####
import sys


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
    array_palavras = []                                                                                                 # Varias Palavras
    array_ocorrencias = [[]]                                                                                            # Ocorrencias/N linhas - String -> Ex.: "1 2 3"

    if sys.stdin.readline() == CMD_IN_TEXTO:
        array_palavras, array_ocorrencias = input_texto(array_palavras, array_ocorrencias)
    else:
        sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)
    input_cmd(array_palavras, array_ocorrencias)

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


def input_cmd(array_palavras, array_ocorrencias):
    # ### FUNCAO ### Le, executa e escreve no stdout os comandos no stdin, ate CMD_IN_TERMINADO
    for linha in sys.stdin:
        if linha == CMD_IN_TERMINADO2:
            break
        elif linha == CMD_IN_TERMINADO:
            break
        elif linha == "":
            break
        elif (CMD_IN_LINHAS in linha) and (linha.index(CMD_IN_LINHAS) == 0):
            palavra = linha[len(CMD_IN_LINHAS)+1:len(linha)-1]
            palavra = palavra.lower()

            indice_palavra = pesquisa_binaria(array_palavras, palavra)
            if not (indice_palavra == -1):
                print(print_array(array_ocorrencias[indice_palavra]))
            else:
                print(CMD_OUT_NULO)
        elif (CMD_IN_ASSOC in linha) and (linha.index(CMD_IN_ASSOC) == 0):
            palavras = linha.split(' ')
            palavras[2] = (palavras[2])[:len(palavras[2])-1]
            palavras[1] = palavras[1].lower()

            indice_palavra = pesquisa_binaria(array_palavras, palavras[1])
            if not (indice_palavra == -1):
                if not (pesquisa_binaria(array_ocorrencias[indice_palavra], int(palavras[2])) == -1):		            # Confirmar Alteracao
                    print(CMD_OUT_ENCONTRADA)
                else:
                    print(CMD_OUT_NAOENCONTRADA)
            else:
                print(CMD_OUT_NAOENCONTRADA)
        else:
            sys.exit("Erro - Interpretacao dos comandos pos-texto")
    return 0


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


def print_array(array):
    # ### FUNCAO ### Transforma os dados num array numa string com espacos
    string = ""
    for num in array:
        string = string + " " + str(num)
    return string[1:]


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
