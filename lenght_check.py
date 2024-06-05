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