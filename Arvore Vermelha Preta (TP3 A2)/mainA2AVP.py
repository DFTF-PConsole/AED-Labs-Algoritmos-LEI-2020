# #### NOTAS #### V1 Abordagem Top-Down, Nao-Recursiva, Percorre 1 vez | Possui Pesquisa Binaria em Arrays
# Arvore VP -> Raiz -> No (Contem Elemento/Dados) -> liga-se a outros Nos


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
COR_VERMELHA = "v"
COR_PRETA = "p"
LADO_ESQ = "e"
LADO_DIR = "d"


# #### FUNCOES ####
class Elemento:                                                                                                         # Elemento = Dados = Palavra + Ocorrencias
    def __init__(self, input_palavra, input_ocorrencias):
        self.palavra = input_palavra
        self.ocorrencias = []
        self.ocorrencias.append(input_ocorrencias)

    def add_ocorrencia(self, count):                                                                                    # Funcao Adicionar Ocorrencias
        if not count == self.ocorrencias[-1]:
            self.ocorrencias.append(count)


class No:                                                                                                               # NO | Arvore VP -> Raiz -> No (Contem Elemento/Dados) -> liga-se a outros Nos
    def __init__(self, input_elemento=None, input_esquerda=None, input_direita=None, input_cor=COR_VERMELHA):
        self.elemento = input_elemento
        self.esquerda = input_esquerda
        self.direita = input_direita
        self.cor = input_cor


class ArvoreVP:                                                                                                         # Arvore VP
    def __init__(self, input_raiz=None):
        self.raiz = input_raiz

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

    def rotacao_simples_esquerda(self, input_no):
        # ### FUNCAO ### Rotacao Simples Esquerda (Direcao <-) | last == DIR
        temp_no = input_no.direita
        input_no.direita = temp_no.esquerda
        temp_no.esquerda = input_no
        input_no.cor = COR_VERMELHA
        temp_no.cor = COR_PRETA
        return temp_no

    def rotacao_simples_direita(self, input_no):
        # ### FUNCAO ### Rotacao Simples Direita ( Direcao ->) | last == ESQ
        temp_no = input_no.esquerda
        input_no.esquerda = temp_no.direita
        temp_no.direita = input_no
        input_no.cor = COR_VERMELHA
        temp_no.cor = COR_PRETA
        return temp_no

    def rotacao_dupla_direita_esquerda(self, input_no):
        # ### FUNCAO ### Rotacao Dupla Direita-Esquerda ( Direcao -> e <-) | last == DIR
        input_no.direita = self.rotacao_simples_direita(input_no.direita)                                               # last = ESQ
        return self.rotacao_simples_esquerda(input_no)                                                                  # last = DIR

    def rotacao_dupla_esquerda_direita(self, input_no):
        # ### FUNCAO ### Rotacao Dupla Esquerda-Direita ( Direcao <- e ->) | last == ESQ
        input_no.esquerda = self.rotacao_simples_esquerda(input_no.esquerda)                                            # last = DIR
        return self.rotacao_simples_direita(input_no)                                                                   # last = ESQ

    def inserir_elemento(self, input_elemento):
        # ### FUNCAO ### Inserir Elementos na Arvore VP
        if self.raiz is None:                                                                                           # Primeiro Elemento da Arvore (Raiz)
            self.raiz = No(input_elemento)
        else:                                                                                                           # Ja Ha Elementos na Arvore
            # Ponteiros: Familia-Nos: bisavo -> avo -> pai -> atual/filho
            no_avo = no_pai = None
            no_temp = No()                                                                                              # No Temporario - Criacao
            no_bisavo = no_temp
            no_bisavo.direita = no_atual = self.raiz

            orientacao_atual = LADO_ESQ                                                                                 # Entre Pai -> Filho
            orientacao_anterior = LADO_ESQ                                                                              # Entre Avo -> Pai
            orientacao_anterior2 = None                                                                                 # Entre Bisavo -> Avo

            while True:                                                                                                 # Navegando na Arvore
                if no_atual is None:                                                                                    # Inserindo no Final da Arvore
                    no_atual = No(input_elemento)
                    if orientacao_atual == LADO_ESQ:
                        no_pai.esquerda = no_atual
                    else:
                        no_pai.direita = no_atual
                else:
                    if (no_atual.esquerda is not None and no_atual.direita is not None) and no_atual.esquerda.cor == COR_VERMELHA and no_atual.direita.cor == COR_VERMELHA:
                        # Se ambos os filhos do no atual sao vermelhos -> trocar para preto nos filhos, no atual fica vermelho
                        no_atual.cor = COR_VERMELHA
                        no_atual.esquerda.cor = COR_PRETA
                        no_atual.direita.cor = COR_PRETA

                # ---------------------------------------------------------------------------
                # Resolver Violacao da Regra: Pai e Filho serem ambos Vermelho
                if (no_atual is not None and no_pai is not None) and no_atual.cor == COR_VERMELHA and no_pai.cor == COR_VERMELHA:
                    # Se e filho sao vermelhos -> fazer rotacoes
                    if no_bisavo.esquerda == no_avo:
                        # Indica a orientacao entre bisavo e avo, para guardar na direcao certa o return das rotacoes
                        orientacao_anterior2 = LADO_ESQ
                    else:
                        orientacao_anterior2 = LADO_DIR

                    if orientacao_anterior == LADO_ESQ:                                                                 # Orientacao Entre Avo e Pai
                        if orientacao_atual == LADO_ESQ:                                                                # Orientacao Entre Pai e Atual/Filho
                            # Se entre Avo-Pai-Filho/Atual -> Esq-Esq
                            if orientacao_anterior2 == LADO_ESQ:
                                no_bisavo.esquerda = self.rotacao_simples_direita(no_avo)
                            else:
                                no_bisavo.direita = self.rotacao_simples_direita(no_avo)
                        else:
                            # Se entre Avo-Pai-Filho/Atual -> Esq-Dir
                            if orientacao_anterior2 == LADO_ESQ:
                                no_bisavo.esquerda = self.rotacao_dupla_esquerda_direita(no_avo)
                            else:
                                no_bisavo.direita = self.rotacao_dupla_esquerda_direita(no_avo)
                    else:
                        if orientacao_atual == LADO_DIR:                                                                # Orientacao Entre Pai e Atual/Filho
                            # Se entre Avo-Pai-Filho/Atual -> Dir-Dir
                            if orientacao_anterior2 == LADO_ESQ:
                                no_bisavo.esquerda = self.rotacao_simples_esquerda(no_avo)
                            else:
                                no_bisavo.direita = self.rotacao_simples_esquerda(no_avo)
                        else:
                            # Se entre Avo-Pai-Filho/Atual -> Dir-Esq
                            if orientacao_anterior2 == LADO_ESQ:
                                no_bisavo.esquerda = self.rotacao_dupla_direita_esquerda(no_avo)
                            else:
                                no_bisavo.direita = self.rotacao_dupla_direita_esquerda(no_avo)
                # ---------------------------------------------------------------------------

                if no_atual.elemento.palavra == input_elemento.palavra:
                    break   # Condicao de Paragem do Ciclo

                # --------------------- Preparar para proxima iteracao do ciclo ------------------------
                if no_avo is not None:                                                                                  # manter no bisavo == raiz ate ter altura para tal
                    no_bisavo = no_avo
                no_avo = no_pai
                no_pai = no_atual

                # Encontrar direcao do caminho a percorrer... Esq. Vs Dir.
                orientacao_anterior = orientacao_atual
                if compara_str(no_atual.elemento.palavra, input_elemento.palavra) == 1:                                 # str-no maior que str-input
                    orientacao_atual = LADO_ESQ
                    no_atual = no_atual.esquerda
                else:                                                                                                   # str-input maior que str-no
                    orientacao_atual = LADO_DIR
                    no_atual = no_atual.direita

            self.raiz = no_temp.direita                                                                                 # No fim do while, dentro do else, nova arvore na raiz
        self.raiz.cor = COR_PRETA                                                                                       # colocar a cor da raiz de preto (regra), pode ter mudado nas rotacoes


def compara_str(str1, str2):
    # ### FUNCAO ### str1 maior: return 1, str2 maior: return 2, iguais: return 0
    if str1 > str2:                                                                                                     # Str1 Maior
        return 1
    elif str1 < str2:                                                                                                   # Str2 Maior
        return 2
    else:                                                                                                               # Iguais
        return 0


def input_texto(arvore_vp):
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
                    elemento = arvore_vp.procura_palavra(palavra)
                    if elemento is not None:
                        elemento.add_ocorrencia(count)
                    else:
                        elemento = Elemento(palavra, count)
                        arvore_vp.inserir_elemento(elemento)
                palavra = ""
            elif ch == ' ' or ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')':
                if len(palavra) > 0:
                    palavra = palavra.lower()
                    elemento = arvore_vp.procura_palavra(palavra)
                    if elemento is not None:
                        elemento.add_ocorrencia(count)
                    else:
                        elemento = Elemento(palavra, count)
                        arvore_vp.inserir_elemento(elemento)
                elemento = arvore_vp.procura_palavra(ch)
                if elemento is not None:
                    elemento.add_ocorrencia(count)
                else:
                    elemento = Elemento(ch, count)
                    arvore_vp.inserir_elemento(elemento)
                palavra = ""
            else:
                palavra = palavra + ch
        count += 1
    print(CMD_OUT_GUARDADO)
    return 0


def input_cmd(arvore_vp):
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
            elemento = arvore_vp.procura_palavra(palavra)
            if elemento is not None:
                print(print_array(elemento.ocorrencias))
            else:
                print(CMD_OUT_NULO)
        elif (CMD_IN_ASSOC in linha) and (linha.index(CMD_IN_ASSOC) == 0):
            palavras = linha.split(' ')
            palavras[2] = (palavras[2])[:len(palavras[2])-1]
            palavras[1] = palavras[1].lower()

            elemento = arvore_vp.procura_palavra(palavras[1])
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
    arvore_vp = ArvoreVP()

    if sys.stdin.readline() == CMD_IN_TEXTO:
        input_texto(arvore_vp)
    else:
        sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)

    input_cmd(arvore_vp)
    return 0


if __name__ == '__main__':
    # ### START ###
    main()

