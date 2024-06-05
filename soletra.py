###############################################################
print("Step 1 - Carrega o arquivo de palavras na memoria")


def extrair_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()
        # Substitua todos os caracteres de pontuação por espaços
        for pontuacao in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            texto = texto.replace(pontuacao, " ")
        # Divida o texto em palavras
        palavras = texto.split()
        return palavras
# Nome do arquivo de texto
arquivo_txt = 'palavras_new.txt'

# Extrai as palavras do arquivo
lista_de_palavras = extrair_palavras(arquivo_txt)

###############################################################
print("Step 2 - inicia e trata o array de letras")

# Recebe todas as letras
letras_permitidas = ["a", "e", "i", "t", "l", "v", "d"]
letra_obrigatoria = "v"
array_letras_portugues = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']

##########

letras_a_remover = letras_permitidas

def remover_letras(letras_a_remover, array_letras):
    for letra in letras_a_remover:
        if letra in array_letras:
            array_letras.remove(letra)
    return array_letras

array_sem_letras = remover_letras(letras_a_remover, array_letras_portugues)

# Print de letras que sao permitidas na busca
print(letras_permitidas)

################################################################
print("Step 3 - Remove palavras que tem letras nao permitidas")

def limpa_palavras(array_sem_letras, lista_de_palavras):
    palavras_filtradas = []
    print("Iniciout funcao")

    for palavra in lista_de_palavras:
        manter_palavra = True

        for letra in array_sem_letras:
            if letra in palavra:
                manter_palavra = False
                break
        if manter_palavra:
            palavras_filtradas.append(palavra)
    return palavras_filtradas

palavras_filtradas_prontas = limpa_palavras(array_sem_letras, lista_de_palavras)

# Mostra o Array pronto
# print(palavras_filtradas_prontas)

################################################################
print("Step 4 - Remove palavras de tamanhos errados")

def verifica_tamanho(palavras_filtradas_prontas):
    palavras_filtradas_tamanho = []
    print("Iniciout funcao verifica_tamanho")

    for palavra in palavras_filtradas_prontas:
        manter_palavra = True
        if len(palavra) < 4:
            manter_palavra = False
        if len(palavra) > 13:
            manter_palavra = False

        if manter_palavra:
            palavras_filtradas_tamanho.append(palavra)
    return palavras_filtradas_tamanho

palavras_filtradas_tamanho = verifica_tamanho(palavras_filtradas_prontas)

# Imprime palavras filtradas por tamanho
# print(palavras_filtradas_tamanho)

################################################################
print("Step 5 - Mantem apenas palavras com a letra obrigatoria")

def verifica_obrigatoria(palavras_filtradas_tamanho):
    respostas = []
    print("Iniciout funcao verifica_obrigatoria")

    for palavra in palavras_filtradas_tamanho:
        manter_palavra = False

        for letra in palavra:
            if letra == letra_obrigatoria:
                manter_palavra = True
                break
        if manter_palavra:
            respostas.append(palavra)
    return respostas

respostas = verifica_obrigatoria(palavras_filtradas_tamanho)

# Imprime as repostas
# print(respostas)

################################################################
print("Step 6 - Print dos resultados")

palavras_4 = []
palavras_5 = []
palavras_6 = []
palavras_7 = []
palavras_8 = []
palavras_9 = []
palavras_10 = []

for palavra in respostas:
    if len(palavra) == 4:
        palavras_4.append(palavra)
for palavra in respostas:
    if len(palavra) == 5:
        palavras_5.append(palavra)
for palavra in respostas:
    if len(palavra) == 6:
        palavras_6.append(palavra)
for palavra in respostas:
    if len(palavra) == 7:
        palavras_7.append(palavra)
for palavra in respostas:
    if len(palavra) == 8:
        palavras_8.append(palavra)
for palavra in respostas:
    if len(palavra) == 9:
        palavras_9.append(palavra)
for palavra in respostas:
    if len(palavra) > 9:
        palavras_10.append(palavra)

def imprime_tudo():
    print("---------------------------------------------------------------------------------")
    print("Letras do dia: " + str(letras_permitidas))
    print("Letra Obrigatoria: " + str(letra_obrigatoria))
    print("---------------------------------------------------------------------------------")
    print("Palavras de 4 letras: ")
    print(palavras_4)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 5 letras: ")
    print(palavras_5)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 6 letras: ")
    print(palavras_6)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 7 letras: ")
    print(palavras_7)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 8 letras: ")
    print(palavras_8)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 9 letras: ")
    print(palavras_9)
    print("---------------------------------------------------------------------------------")
    print("Palavras de muitas muitas letras: ")
    print(palavras_10)
    print("---------------------------------------------------------------------------------")
    print("xXxXxX")
    print("---------------------------------------------------------------------------------")

imprime_tudo()