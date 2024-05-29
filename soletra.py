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
arquivo_txt = 'palavras.txt'

# Extrai as palavras do arquivo
lista_de_palavras = extrair_palavras(arquivo_txt)

###############################################################
print("Step 2 - inicia e trata o array de letras")

# Recebe todas as letras
letras_permitidas = ["a", "u", "o", "d", "ç", "r", "p"]
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

print("Gerou o array pronto")
palavras_filtradas_prontas = limpa_palavras(array_sem_letras, lista_de_palavras)

# Mostra o Array pronto
# print(palavras_filtradas_prontas)




# palavras_restantes = limpa_palavras(letrinha, lista_de_palavras)
# Imprime a lista de palavras total que sobraram   
                
##################



