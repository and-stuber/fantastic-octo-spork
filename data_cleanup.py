def limpa_palavras(array_sem_letras, lista_de_palavras):
    palavras_filtradas = []

    for palavra in lista_de_palavras:
        manter_palavra = True

        for letra in array_sem_letras:
            if letra in palavra:
                manter_palavra = False
                break
        if manter_palavra:
            palavras_filtradas.append(palavra)
    return palavras_filtradas
