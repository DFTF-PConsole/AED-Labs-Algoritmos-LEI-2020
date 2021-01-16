import sys

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


def main():
    array_palavras = []                                                                                                 # Varias Palavras
    array_ocorrencias = []                                                                                              # Ocorrencias/N linhas - String -> Ex.: "1 2 3"

    if sys.stdin.readline() == CMD_IN_TEXTO:
        input_texto(array_palavras, array_ocorrencias)
    else:
        sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)

    # for i in range(len(array_palavras)):  # debug
        # print(array_palavras[i] + " | " + array_ocorrencias[i]) # debug

    input_cmd(array_palavras, array_ocorrencias)
    return 0


def input_texto(array_palavras, array_ocorrencias):
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
                    if palavra in array_palavras:
                        if not (str(count) in array_ocorrencias[array_palavras.index(palavra)]):
                            array_ocorrencias[array_palavras.index(palavra)] = array_ocorrencias[array_palavras.index(palavra)] + " " + str(count)
                    else:
                        array_palavras.append(palavra)
                        array_ocorrencias.append(str(count))
                palavra = ""
            elif ch == ' ' or ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')':
                if len(palavra) > 0:
                    palavra = palavra.lower()
                    if palavra in array_palavras:
                        if not (str(count) in array_ocorrencias[array_palavras.index(palavra)]):
                            array_ocorrencias[array_palavras.index(palavra)] = array_ocorrencias[array_palavras.index(palavra)] + " " + str(count)
                    else:
                        array_palavras.append(palavra)
                        array_ocorrencias.append(str(count))
                if ch in array_palavras:
                    if not (str(count) in array_ocorrencias[array_palavras.index(ch)]):
                        array_ocorrencias[array_palavras.index(ch)] = array_ocorrencias[array_palavras.index(ch)] + " " + str(count)
                else:
                    array_palavras.append(ch)
                    array_ocorrencias.append(str(count))
                palavra = ""
            else:
                palavra = palavra + ch
        count += 1
    print(CMD_OUT_GUARDADO)
    return 0


def input_cmd(array_palavras, array_ocorrencias):
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
            # print(palavra) # debug
            if palavra in array_palavras:
                print(array_ocorrencias[array_palavras.index(palavra)])
            else:
                print(CMD_OUT_NULO)
        elif (CMD_IN_ASSOC in linha) and (linha.index(CMD_IN_ASSOC) == 0):
            palavras = linha.split(' ')
            palavras[2] = (palavras[2])[:len(palavras[2])-1]
            palavras[1] = palavras[1].lower()
            if palavras[1] in array_palavras:
                if palavras[2] in array_ocorrencias[array_palavras.index(palavras[1])].split(' '):		                # Confirmar Alteracao
                    print(CMD_OUT_ENCONTRADA)
                else:
                    print(CMD_OUT_NAOENCONTRADA)
            else:
                print(CMD_OUT_NAOENCONTRADA)
        else:
            sys.exit("Erro - Interpretacao dos comandos pos-texto")
    return 0


if __name__ == '__main__':
    main()
