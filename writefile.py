def grava_resultados(data):
    with open ("./data/results.txt", "w", encoding="utf-8") as arquivo:
        for palavra in data:
            arquivo.write(palavra + "\n")
    return("Arquivo gravado...")
    