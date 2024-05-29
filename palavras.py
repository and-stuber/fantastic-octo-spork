def encontrar_letra(palavras, letra):
    palavras_com_letra = []
    for palavra in palavras:
        if letra in palavra:
            palavras_com_letra.append(palavra)
    return palavras_com_letra

# Exemplo de uso
lista_de_palavras = ["casa", "carro", "banana", "mamão", "abacaxi"]
letra_procurada = "a"
resultado = encontrar_letra(lista_de_palavras, letra_procurada)
print("Palavras que contêm a letra '{}':".format(letra_procurada))
print(resultado)