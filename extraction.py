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
arquivo_txt = './data/palavras_new.txt'
print("Lendo aquivo: " + arquivo_txt)

# Extrai as palavras do arquivo
print("Gerando lista...")
lista_de_palavras = extrair_palavras(arquivo_txt)
print("Lista pronta")