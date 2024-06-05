def grava_resultados(data):
    with open ("results.txt", "w", encoding="utf-8") as arquivo:
        for palavra in data:
            arquivo.write(palavra + "\n")
    return("Arquivo gravado...")
    