def verifica_obrigatoria(palavras_filtradas_tamanho, letra_obrigatoria):
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
