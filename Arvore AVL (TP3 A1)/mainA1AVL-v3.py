# v3 - Melhoramentos: Retirei "in" em "x in array"; implementei pesquisa binaria; print_array; etc.
# v3 Abordagem Ate as folhas, depois de Baixo-para-Cima, Recursiva
# pai.direcao = return no filho da recursividade


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
class Elemento:
    def __init__(self, input_palavra, input_ocorrencias):
        self.palavra = input_palavra
        self.ocorrencias = []
        self.ocorrencias.append(input_ocorrencias)

    def add_ocorrencia(self, count):
        if not count == self.ocorrencias[-1]:
            self.ocorrencias.append(count)


class No:
    def __init__(self, input_elemento=None, input_esquerda=None, input_direita=None):
        self.elemento = input_elemento
        self.esquerda = input_esquerda
        self.direita = input_direita
        self.altura = 1


class ArvoreAVL:
    def __init__(self, input_raiz=None):
        self.raiz = input_raiz

    def rotacao_esq(self, input_no_k1):                                                                                 # Faz rotacao simples com filho k2 a direita, E <- D
        # ### FUNCAO ### Rotacao Simples Esquerda (Direcao <-)
        no_k2 = input_no_k1.direita
        no_k3 = no_k2.esquerda
        no_k2.esquerda = input_no_k1
        input_no_k1.direita = no_k3
        input_no_k1.altura = 1 + max(self.get_altura(input_no_k1.esquerda), self.get_altura(input_no_k1.direita))       # Cumprir ordem para obter altura coerente
        no_k2.altura = 1 + max(self.get_altura(no_k2.esquerda), self.get_altura(no_k2.direita))                         # Altura anterior + 1 (para incluir o no atual)
        return no_k2                                                                                                    # Nova raiz da sub-arvore

    def rotacao_dir(self, input_no_k1):                                                                                 # Faz rotacao simples com filho k2 a esquerda, E -> D
        # ### FUNCAO ### Rotacao Simples Direita ( Direcao ->)
        no_k2 = input_no_k1.esquerda
        no_k3 = no_k2.direita
        no_k2.direita = input_no_k1
        input_no_k1.esquerda = no_k3
        input_no_k1.altura = 1 + max(self.get_altura(input_no_k1.esquerda), self.get_altura(input_no_k1.direita))
        no_k2.altura = 1 + max(self.get_altura(no_k2.esquerda), self.get_altura(no_k2.direita))
        return no_k2

    def rotacao_esq_dir(self, input_no_k1):                                                                             # Faz rotacao com filho k2 a direita | Faz rotacao com filho k2 a esquerda ?
        # ### FUNCAO ### Rotacao Dupla Esquerda-Direita ( Direcao <- e ->)
        input_no_k1.esquerda = self.rotacao_esq(input_no_k1.esquerda)
        return self.rotacao_dir(input_no_k1)

    def rotacao_dir_esq(self, input_no_k1):                                                                             # Faz rotacao com filho k2 a esquerda | Faz rotacao com filho k2 a direita ?
        # ### FUNCAO ### Rotacao Dupla Direita-Esquerda ( Direcao -> e <-)
        input_no_k1.direita = self.rotacao_dir(input_no_k1.direita)
        return self.rotacao_esq(input_no_k1)

    def procura_palavra(self, input_palavra):
        # ### FUNCAO ### Procura Palavra na Arvore e return esse elemento, se nao existe retorna: None
        no = self.raiz
        while no is not None:
            if compara_str(input_palavra, no.elemento.palavra) == 0:
                return no.elemento
            elif compara_str(input_palavra, no.elemento.palavra) == 1:
                no = no.direita
            else:
                no = no.esquerda
        return None

    def inserir_elemento(self, input_raiz, input_elemento):                                                             # input_raiz -> raiz ou no da sub-arvore
        # ### FUNCAO ### Inserir Elementos na Arvore AVP, recursivamente, ate chegar as folhas nulas, inserindo-o
        if input_raiz is None:                                                                                          # Insere o elemento
            novo_no = No(input_elemento)
            return novo_no
        elif compara_str(input_raiz.elemento.palavra, input_elemento.palavra) == 1:                                     # Se a str 1 (no da arvore) e maior
            input_raiz.esquerda = self.inserir_elemento(input_raiz.esquerda, input_elemento)
        else:                                                                                                           # Se a str 2 (novo no) e maior
            input_raiz.direita = self.inserir_elemento(input_raiz.direita, input_elemento)

        input_raiz.altura = 1 + max(self.get_altura(input_raiz.esquerda), self.get_altura(input_raiz.direita))          # Altura anterior + 1 (para incluir o no atual)

        # ----------------------- Verificar Equilibrio, fazer rotacoes para corrigir ----------------------
        equilibrio = self.get_equilibrio(input_raiz)

        if equilibrio > 1:                                                                                              # Lado Esquerdo MAIOR que o Direito (na sub-arvore do no atual: input_raiz)
            if compara_str(input_raiz.esquerda.elemento.palavra, input_elemento.palavra) == 1:                          # str 1 (Palavra no->esquerdo) MAIOR que str 2 (Palavra nova inserida)
                # Se Caminho entre Avo-Pai-Filho -> Esq-Esq
                return self.rotacao_dir(input_raiz)
            else:                                                                                                       # str 2 (Palavra nova inserida) MAIOR que str 1 (Palavra no->esquerdo)
                # Se Caminho entre Avo-Pai-Filho -> Esq-Dir
                return self.rotacao_esq_dir(input_raiz)
        if equilibrio < -1:                                                                                             # Lado Direito MAIOR que o Esquerdo (na sub-arvore do no atual: input_raiz)
            if compara_str(input_raiz.direita.elemento.palavra, input_elemento.palavra) == 2:                           # str 1 (Palavra no->esquerdo) MAIOR que str 2 (Palavra nova inserida)
                # Se Caminho entre Avo-Pai-Filho -> Dir-Dir
                return self.rotacao_esq(input_raiz)
            else:                                                                                                       # str 2 (Palavra nova inserida) MAIOR que str 1 (Palavra no->esquerdo)
                # Se Caminho entre Avo-Pai-Filho -> Dir-Esq
                return self.rotacao_dir_esq(input_raiz)

        return input_raiz                                                                                               # Sem rotacoes

    def get_altura(self, input_no):
        # ### FUNCAO ### Get Altura guardado no atributo do no, ou 0 se o no e nulo
        if input_no is None:
            return 0
        return input_no.altura

    def get_equilibrio(self, input_no):
        # ### FUNCAO ### Get Equilibrio atraves da altura guardado no atributo do no, ou 0 se o no e nulo
        if input_no is None:
            return 0
        return self.get_altura(input_no.esquerda) - self.get_altura(input_no.direita)                                   # Equilibrio da sub-arvore


def compara_str(str1, str2):
    # ### FUNCAO ### str1 maior: return 1, str2 maior: return 2, iguais: return 0
    if str1 > str2:                                                                                                     # Str1 Maior
        return 1
    elif str1 < str2:                                                                                                   # Str2 Maior
        return 2
    else:                                                                                                               # Iguais
        return 0


def input_texto(arvore_avl):
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
            elemento = arvore_avl.procura_palavra(palavra)
            if elemento is not None:
                print(print_array(elemento.ocorrencias))
            else:
                print(CMD_OUT_NULO)
        elif (CMD_IN_ASSOC in linha) and (linha.index(CMD_IN_ASSOC) == 0):
            palavras = linha.split(' ')
            palavras[2] = (palavras[2])[:len(palavras[2])-1]
            palavras[1] = palavras[1].lower()

            elemento = arvore_avl.procura_palavra(palavras[1])
            if elemento is not None:
                if not (pesquisa_binaria(elemento.ocorrencias, int(palavras[2])) == -1):
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
        if array[meio] == valor:                                                                                        # Valor esta no meio
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


def main():
    # ### FUNCAO ### Funcao Principal
    arvore_avl = ArvoreAVL()
    if sys.stdin.readline() == CMD_IN_TEXTO:
        input_texto(arvore_avl)
    else:
        sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)

    input_cmd(arvore_avl)
    return 0


if __name__ == '__main__':
    # ### START ###
    main()

