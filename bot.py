import pyautogui
import time

# Caminho para o seu arquivo com palavras
arquivo_palavras = './data/results.txt'

# Ler as palavras do arquivo
with open(arquivo_palavras, 'r', encoding="utf-8") as f:
    palavras = f.readlines()

def ordenar_por_tamanho(palavras):
    return sorted(palavras, key=len)

# Ordenar as palavras por comprimento
palavras_ordenadas = ordenar_por_tamanho(palavras)
quantas = len(palavras_ordenadas)
print("Palavras: " + str(quantas))
tempo = quantas * 2 / 60
print("Vai demorar " + str(tempo) + " minutos")

# Esperar alguns segundos para dar tempo de focar no campo de entrada desejado
print("Você tem 2 segundos para focar no campo de entrada desejado...")
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

counter = 0
# Digitar cada palavra e pressionar Enter
for palavra in palavras_ordenadas:
    counter = counter + 1
    print(palavra + " " + str(len(palavra) - 1) + " letras " + str(counter) +"/" + str(quantas))
    pyautogui.typewrite(palavra.strip())
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)  # Ajuste o tempo conforme necessário para evitar problemas de sincronização
