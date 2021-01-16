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


class Elemento:
    def __init__(self, input_palavra, input_ocorrencias):
        self.palavra = input_palavra
        self.ocorrencias = str(input_ocorrencias)

    def add_ocorrencia(self, count):
        if not (str(count) in self.ocorrencias):
            self.ocorrencias = self.ocorrencias + " " + str(count)


class No:
    def __init__(self, input_elemento=None, input_esquerda=None, input_direita=None):
        self.elemento = input_elemento
        self.esquerda = input_esquerda
        self.direita = input_direita
        self.altura = 1


class ArvoreAVL:
    def __init__(self, input_raiz=None):
        self.raiz = input_raiz

    def rotacao_esq(self, input_no_k1):    # Faz rotacao simples com filho k2 a direita, E <- D
        no_k2 = input_no_k1.direita
        no_k3 = no_k2.esquerda
        no_k2.esquerda = input_no_k1
        input_no_k1.direita = no_k3
        input_no_k1.altura = 1 + max(self.get_altura(input_no_k1.esquerda), self.get_altura(input_no_k1.direita))
        no_k2.altura = 1 + max(self.get_altura(no_k2.esquerda), self.get_altura(no_k2.direita))
        return no_k2

    def rotacao_dir(self, input_no_k1):    # Faz rotacao simples com filho k2 a esquerda, E -> D
        no_k2 = input_no_k1.esquerda
        no_k3 = no_k2.direita
        no_k2.direita = input_no_k1
        input_no_k1.esquerda = no_k3
        input_no_k1.altura = 1 + max(self.get_altura(input_no_k1.esquerda), self.get_altura(input_no_k1.direita))
        no_k2.altura = 1 + max(self.get_altura(no_k2.esquerda), self.get_altura(no_k2.direita))
        return no_k2

    def rotacao_esq_dir(self, input_no_k1):    # Faz rotacao com filho k2 a direita | Faz rotacao com filho k2 a esquerda ?
        input_no_k1.esquerda = self.rotacao_esq(input_no_k1.esquerda)
        return self.rotacao_dir(input_no_k1)

    def rotacao_dir_esq(self, input_no_k1):    # Faz rotacao com filho k2 a esquerda | Faz rotacao com filho k2 a direita ?
        input_no_k1.direita = self.rotacao_dir(input_no_k1.direita)
        return self.rotacao_esq(input_no_k1)

    def procura_palavra(self, input_palavra):
        no = self.raiz
        while no is not None:
            if compara_str(input_palavra, no.elemento.palavra) == 0:
                return no.elemento
            elif compara_str(input_palavra, no.elemento.palavra) == 1:
                no = no.direita
            else:
                no = no.esquerda
        return None

    def inserir_elemento(self, input_raiz, input_elemento):
        if input_raiz is None:
            novo_no = No(input_elemento)
            return novo_no
        elif compara_str(input_raiz.elemento.palavra, input_elemento.palavra) == 1:
            input_raiz.esquerda = self.inserir_elemento(input_raiz.esquerda, input_elemento)
        else:
            input_raiz.direita = self.inserir_elemento(input_raiz.direita, input_elemento)

        input_raiz.altura = 1 + max(self.get_altura(input_raiz.esquerda), self.get_altura(input_raiz.direita))

        equilibrio = self.get_equilibrio(input_raiz)

        if equilibrio > 1 and compara_str(input_raiz.esquerda.elemento.palavra, input_elemento.palavra) == 1:      # Rotacao a Esq, Direcao Direita -> Esq > 1 e Raiz > NovoElemento
            return self.rotacao_dir(input_raiz)
        elif equilibrio < -1 and compara_str(input_raiz.direita.elemento.palavra, input_elemento.palavra) == 2:   # Rotacao a Dir, Direcao Direita -> Dir > 1 (Dir < -1)  e Raiz < NovoElemento
            return self.rotacao_esq(input_raiz)
        elif equilibrio > 1 and compara_str(input_raiz.esquerda.elemento.palavra, input_elemento.palavra) == 2:   # Esq Dir
            return self.rotacao_esq_dir(input_raiz)
        elif equilibrio < -1 and compara_str(input_raiz.direita.elemento.palavra, input_elemento.palavra) == 1:   # Dir Esq
            return self.rotacao_dir_esq(input_raiz)
        else:
            return input_raiz

    def get_altura(self, input_no):
        if input_no is None:
            return 0
        return input_no.altura

    def get_equilibrio(self, input_no):
        if input_no is None:
            return 0
        return self.get_altura(input_no.esquerda) - self.get_altura(input_no.direita)


def compara_str(str1, str2):
    if str1 > str2:     # Str1 Maior
        return 1
    elif str1 < str2:   # Str2 Maior
        return 2
    else:               # Iguais
        return 0


def input_texto(arvore_avl):
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
                    elemento = arvore_avl.procura_palavra(palavra)
                    if elemento is not None:
                        elemento.add_ocorrencia(count)
                    else:
                        elemento = Elemento(palavra, count)
                        arvore_avl.raiz = arvore_avl.inserir_elemento(arvore_avl.raiz, elemento)
                palavra = ""
            elif ch == ' ' or ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')':
                if len(palavra) > 0:
                    palavra = palavra.lower()
                    elemento = arvore_avl.procura_palavra(palavra)
                    if elemento is not None:
                        elemento.add_ocorrencia(count)
                    else:
                        elemento = Elemento(palavra, count)
                        arvore_avl.raiz = arvore_avl.inserir_elemento(arvore_avl.raiz, elemento)
                elemento = arvore_avl.procura_palavra(ch)
                if elemento is not None:
                    elemento.add_ocorrencia(count)
                else:
                    elemento = Elemento(ch, count)
                    arvore_avl.raiz = arvore_avl.inserir_elemento(arvore_avl.raiz, elemento)
                palavra = ""
            else:
                palavra = palavra + ch
        count += 1
    print(CMD_OUT_GUARDADO)
    return 0


def input_cmd(arvore_avl):
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
            elemento = arvore_avl.procura_palavra(palavra)
            if elemento is not None:
                print(elemento.ocorrencias)
            else:
                print(CMD_OUT_NULO)
        elif (CMD_IN_ASSOC in linha) and (linha.index(CMD_IN_ASSOC) == 0):
            palavras = linha.split(' ')
            palavras[2] = (palavras[2])[:len(palavras[2])-1]
            palavras[1] = palavras[1].lower()

            elemento = arvore_avl.procura_palavra(palavras[1])
            if elemento is not None:
                if palavras[2] in elemento.ocorrencias.split(' '):
                    print(CMD_OUT_ENCONTRADA)
                else:
                    print(CMD_OUT_NAOENCONTRADA)
            else:
                print(CMD_OUT_NAOENCONTRADA)
        else:
            sys.exit("Erro - Interpretacao dos comandos pos-texto")
    return 0


def main():
    arvore_avl = ArvoreAVL()
    if sys.stdin.readline() == CMD_IN_TEXTO:
        input_texto(arvore_avl)
    else:
        sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)

    input_cmd(arvore_avl)
    return 0


if __name__ == '__main__':
    main()

