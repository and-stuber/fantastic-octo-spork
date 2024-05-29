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
palavras = extrair_palavras(arquivo_txt)

# Imprime as palavras como um array
print(palavras)