# #### NOTAS #### V1 Abordagem: Percorre ate as folhas, insere, e depois traz-lo para a raz (splaying)
# Possui Pesquisa Binaria em Arrays
# Arvore Splay
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
acumula_rotacoes_simples = 0
fator_rotacoes_input = 0


# #### FUNCOES ####
class Elemento:          # Elemento = Dados = Palavra + Ocorrencias
    def __init__(self, input_palavra, input_ocorrencias):
        self.palavra = input_palavra
        self.ocorrencias = []
        self.ocorrencias.append(input_ocorrencias)

    def add_ocorrencia(self, count):           # Funcao Adicionar Ocorrencias
        if not count == self.ocorrencias[-1]:
            self.ocorrencias.append(count)


class No:             # NO | Arvore Splay -> Raiz -> No (Contem Elemento/Dados) -> liga-se a outros Nos
    def __init__(self, input_elemento=None, input_esquerda=None, input_direita=None, input_pai=None):
        self.elemento = input_elemento
        self.esquerda = input_esquerda
        self.direita = input_direita
        self.pai = input_pai


class ArvoreSplay:       # Arvore Splay
    def __init__(self, input_raiz=None):
        self.raiz = input_raiz

    def procura_palavra(self, input_palavra):
        # ### FUNCAO ### Procura Palavra na Arvore e return esse elemento, se nao existe retorna: None
        no = self.raiz
        while no is not None:
            if compara_str(input_palavra, no.elemento.palavra) == 0:  # Palavra Encontrada
                self.splaying(no)     # Traz-lo para a raiz
                return no.elemento
            elif compara_str(input_palavra, no.elemento.palavra) == 1:  # Pesquisa, input MAIOR que no
                no = no.direita
            else:
                no = no.esquerda
        return None         # Palavra nao encontrada

    def rotacao_esquerda(self, no_x):
        # ### FUNCAO ### Rotacao Simples Esquerda (Direcao ->)
        global acumula_rotacoes_simples
        global fator_rotacoes_input
        if fator_rotacoes_input == 1:
            acumula_rotacoes_simples = acumula_rotacoes_simples + 1
        no_y = no_x.direita
        no_x.direita = no_y.esquerda
        no_y.pai = no_x.pai
        if no_y.esquerda is not None:
            no_y.esquerda.pai = no_x    # no_x PAI do no_y-esquerdo
        if no_y.pai is None:
            self.raiz = no_y     # Se x era raiz, agora y e RAIZ
        else:
            if no_x == no_x.pai.esquerda:     # Se X era filho lado ESQ, set pai->y
                no_x.pai.esquerda = no_y
            else:                                # Se X era filho lado DIR, set pai->y
                no_x.pai.direita = no_y
        no_y.esquerda = no_x
        no_x.pai = no_y        # X filho de y

    def rotacao_direita(self, no_x):
        # ### FUNCAO ### Rotacao Simples Direita (Direcao <-)
        global acumula_rotacoes_simples
        global fator_rotacoes_input
        if fator_rotacoes_input == 1:
            acumula_rotacoes_simples = acumula_rotacoes_simples + 1
        no_y = no_x.esquerda
        no_x.esquerda = no_y.direita
        no_y.pai = no_x.pai
        if no_y.direita is not None:
            no_y.direita.pai = no_x   # no_x e PAI do no_y-direito
        if no_y.pai is None:
            self.raiz = no_y     # Se x era raiz, agora y e RAIZ
        else:
            if no_x == no_x.pai.direita: # Se X era filho lado DIR, set pai->y
                no_x.pai.direita = no_y
            else:          # Se X era filho lado ESQ, set pai->y
                no_x.pai.esquerda = no_y
        no_y.direita = no_x
        no_x.pai = no_y             # X filho de y

    def splaying(self, no_atual):
        # ### FUNCAO ### Trazer o no_atual para a raiz atraves de rotacoes
        while no_atual.pai is not None:    # Enquanto o no_atual nao e a raiz...
            if no_atual.pai == self.raiz:      # No_atual filho do no-raiz
                if no_atual == self.raiz.esquerda:
                    # no_atual FILHO ESQ | ZIG - Rotacao Simples DIR (Direcao <-)
                    self.rotacao_direita(no_atual.pai)
                else:
                    # no_atual FILHO DIR | ZIG - Rotacao Simples ESQ (Direcao ->)
                    self.rotacao_esquerda(no_atual.pai)
            else:               # No_atual ainda nao e filho do no-raiz
                no_pai = no_atual.pai         # Ponteiros: Familia-Nos: avo -> pai -> atual/filho
                no_avo = no_atual.pai.pai
                if no_avo.esquerda == no_pai:
                    if no_pai.esquerda == no_atual:
                        # avo-pai-no_atual -> ESQ - ESQ | ZIG ZIG - Rotacao Dupla DIR (Direcao <- <-)
                        self.rotacao_direita(no_avo)  # Porque no_avo ou no_pai? ver slides Prof, g=avo e p=pai e x=no_atual
                        self.rotacao_direita(no_pai)
                    if no_pai.direita == no_atual:
                        # avo-pai-no_atual -> ESQ - DIR | ZIG ZAG - Rotacao ESQ DIR (Direcao -> <-)
                        self.rotacao_esquerda(no_pai)
                        self.rotacao_direita(no_avo)
                if no_avo.direita == no_pai:
                    if no_pai.esquerda == no_atual:
                        # avo-pai-no_atual -> DIR - ESQ | ZIG ZAG - Rotacao DIR ESQ (Direcao <- ->)
                        self.rotacao_direita(no_pai)
                        self.rotacao_esquerda(no_avo)
                    if no_pai.direita == no_atual:
                        # avo-pai-no_atual -> DIR - DIR | ZIG ZIG - Rotacao Dupla ESQ (Direcao -> ->)
                        self.rotacao_esquerda(no_avo)
                        self.rotacao_esquerda(no_pai)

    def inserir_elemento(self, input_elemento):
        # ### FUNCAO ### Inserir Elementos na Arvore Splay
        novo_no = No(input_elemento)
        if self.raiz is None:    # Se primeiro elemento na arvore
            self.raiz = novo_no
            return
        no_pai = temp_no = self.raiz
        while temp_no is not None:     # Encontra final da arvore (folha) a ser colocado novo_no
            no_pai = temp_no           # Encontra Futuro No-Pai
            if compara_str(temp_no.elemento.palavra, input_elemento.palavra) == 1:   # str1 (No da Arvore) MAIOR
                temp_no = temp_no.esquerda
            else:                                # str2 (No Novo) MAIOR
                temp_no = temp_no.direita
        novo_no.pai = no_pai
        if compara_str(no_pai.elemento.palavra, input_elemento.palavra) == 1:    # str1 (No da Arvore) MAIOR
            no_pai.esquerda = novo_no
        else:                          # str2 (No Novo) MAIOR
            no_pai.direita = novo_no
        self.splaying(novo_no)           # Traz-lo para a raiz


def compara_str(str1, str2):
    # ### FUNCAO ### str1 maior: return 1, str2 maior: return 2, iguais: return 0
    if str1 > str2:          # Str1 Maior
        return 1
    elif str1 < str2:       # Str2 Maior
        return 2
    else:                       # Iguais
        return 0


def input_texto(arvore_splay):
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
                    elemento = arvore_splay.procura_palavra(palavra)
                    if elemento is not None:
                        elemento.add_ocorrencia(count)
                    else:
                        elemento = Elemento(palavra, count)
                        arvore_splay.inserir_elemento(elemento)
                palavra = ""
            elif ch == ' ' or ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')':
                if len(palavra) > 0:
                    palavra = palavra.lower()
                    elemento = arvore_splay.procura_palavra(palavra)
                    if elemento is not None:
                        elemento.add_ocorrencia(count)
                    else:
                        elemento = Elemento(palavra, count)
                        arvore_splay.inserir_elemento(elemento)
                elemento = arvore_splay.procura_palavra(ch)
                if elemento is not None:
                    elemento.add_ocorrencia(count)
                else:
                    elemento = Elemento(ch, count)
                    arvore_splay.inserir_elemento(elemento)
                palavra = ""
            else:
                palavra = palavra + ch
        count += 1
    print(CMD_OUT_GUARDADO)
    return 0


def input_cmd(arvore_splay):
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
            elemento = arvore_splay.procura_palavra(palavra)
            if elemento is not None:
                print(print_array(elemento.ocorrencias))
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

            elemento = arvore_splay.procura_palavra(palavras[1])
            if elemento is not None:
                if not (pesquisa_binaria(elemento.ocorrencias, int(palavras[2])) == -1):
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
        meio = inicio + (fim - inicio) // 2         # Divisao Real, Arredonda para baixo
        if array[meio] == valor:                       # Valor esta no meio
            return meio
        elif array[meio] < valor:          # Se valor e maior que o meio, ignora metade inferior
            inicio = meio + 1
        else:                                             # Se for menor que o meio, ignora metade superior
            fim = meio - 1
    return -1                                   # Nao existe


def print_array(array):
    # ### FUNCAO ### Transforma os dados num array numa string com espacos
    string = ""
    for num in array:
        string = string + " " + str(num)
    return string[1:]


def main():
    # ### FUNCAO ### Funcao Principal
    textos_relatorio = ["A", "B", "C", "D"]
    global acumula_linhas
    global acumula_assoc
    global acumula_rotacoes_simples
    global fator_rotacoes_input
    for n_texto in textos_relatorio:
        print("# # # # # # TEXTO " + n_texto + " # # # # # #")
        acumula_texto = 0
        acumula_linhas = 0
        acumula_assoc = 0
        acumula_rotacoes_simples = 0
        for i in range(20):
            arvore_splay = ArvoreSplay()
            while msvcrt.kbhit():  # Clean stdin Windows
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
                fator_rotacoes_input = 1
                input_texto(arvore_splay)
                fator_rotacoes_input = 0
                end_texto = time.time()
                tempo_texto = end_texto - start_texto
            else:
                sys.exit("Erro - Sem Comando Incial: " + CMD_IN_TEXTO)
            input_cmd(arvore_splay)
            acumula_texto = acumula_texto + tempo_texto
            print("#########################################\n")
        acumula_texto = acumula_texto / 20.0
        acumula_linhas = acumula_linhas / 20.0
        acumula_assoc = acumula_assoc / 20.0
        acumula_rotacoes_simples = acumula_rotacoes_simples // 20  # Porque contou 20 vezes
        print("* * * * * Tempo Medio em Segundos Input TEXTO = " + str(acumula_texto) + " * * * * *")
        print("* * * * * Rotacoes Simples - Input TEXTO = " + str(acumula_rotacoes_simples) + " * * * * *")
        print("* * * * * Tempo Medio em Segundos Input CMDs - LINHAS = " + str(acumula_linhas) + " * * * * *")
        print("* * * * * Tempo Medio em Segundos Input CMDs - ASSOC = " + str(acumula_assoc) + " * * * * *")
        print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n\n")
    return 0


if __name__ == '__main__':
    # ### START ###
    main()
