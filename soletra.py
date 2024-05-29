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

# Recebe todas as letras
letras_permitidas = ["a", "u", "o", "d", "ç", "r", "o", "p"]
array_letras_portugues = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']

###############################################################

letras_a_remover = letras_permitidas

def remover_letras(letras_a_remover, array_letras):
    for letra in letras_a_remover:
        if letra in array_letras:
            array_letras.remove(letra)
    return array_letras

array_sem_letras = remover_letras(letras_a_remover, array_letras_portugues)

print(array_sem_letras)










def encontrar_letra(palavras, letra):
    palavras_com_letra = []
    for palavra in palavras:
        if letra in palavra:
            palavras_com_letra.append(palavra)
    return palavras_com_letra

# Exemplo de uso



resultado = encontrar_letra(lista_de_palavras, letra_procurada)
print("Palavras que contêm a letra '{}':".format(letra_procurada))
print(resultado)