from datetime import datetime
from extraction import extrair_palavras
from context import  remover_letras
from data_cleanup import limpa_palavras
from lenght_check import verifica_tamanho
from check_main import verifica_obrigatoria
from writefile import grava_resultados
from bot_unicode import results_to_unicode

########## 1
# Nome do arquivo de texto
arquivo_txt = './data/new_worlds_list.txt'

# Extrai as palavras do arquivo
print(str(datetime.now().time()) + " Gerando lista...")
lista_de_palavras = extrair_palavras(arquivo_txt)
print(str(datetime.now().time()) + " Lista pronta")

########## 2
# Recebe todas as letras
letras_permitidas = ["a", "e", "u", "r", "c", "t", "z"]
letra_obrigatoria = "u"
array_letras_portugues = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']

letras_a_remover = letras_permitidas

array_sem_letras = remover_letras(letras_a_remover, array_letras_portugues)

# Print de letras que sao permitidas na busca e letras removidas
print("Letras Permitidas: " + str(letras_permitidas))
print("Letras removidas: " + str(array_sem_letras))

########## 3
# Limpando as palavras que nao serao uteis
print(str(datetime.now().time()) + " Filtrando palavras ")


palavras_filtradas_prontas = limpa_palavras(array_sem_letras, lista_de_palavras)
print(str(datetime.now().time()) + " Filtrando palavras (Terminou) ")
# Mostra o Array pronto
# print(palavras_filtradas_prontas)

########## 4
print(str(datetime.now().time()) + " Removendo palavras de tamanhos errados")

palavras_filtradas_tamanho = verifica_tamanho(palavras_filtradas_prontas)

########## 5
print(str(datetime.now().time()) + " Mantem apenas palavras com a letra obrigatoria")

respostas = verifica_obrigatoria(palavras_filtradas_tamanho, letra_obrigatoria)

########## 6
print(str(datetime.now().time()) + " Gravando aquivo de respostas")

grava_resultados(respostas)

# print("E tambem unidecode....")
# results_to_unicode()

########## 7
################################################################
finish = datetime.now().time()

print ("Fim da execucao " + str(finish))
breakpoint
print("----------------------------- Resultados -----------------------------")

palavras_4 = []
palavras_5 = []
palavras_6 = []
palavras_7 = []
palavras_8 = []
palavras_9 = []
palavras_10 = []

for palavra in respostas:
    if len(palavra) == 4:
        palavras_4.append(palavra)
for palavra in respostas:
    if len(palavra) == 5:
        palavras_5.append(palavra)
for palavra in respostas:
    if len(palavra) == 6:
        palavras_6.append(palavra)
for palavra in respostas:
    if len(palavra) == 7:
        palavras_7.append(palavra)
for palavra in respostas:
    if len(palavra) == 8:
        palavras_8.append(palavra)
for palavra in respostas:
    if len(palavra) == 9:
        palavras_9.append(palavra)
for palavra in respostas:
    if len(palavra) > 9:
        palavras_10.append(palavra)

def imprime_tudo():
    print("---------------------------------------------------------------------------------")
    print("Letras do dia: " + str(letras_permitidas))
    print("Letra Obrigatoria: " + str(letra_obrigatoria))
    print("Total de Palavras: " + str(len(respostas)))
    print("---------------------------------------------------------------------------------")
    print("Palavras de 4 letras: ")
    print(palavras_4)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 5 letras: ")
    print(palavras_5)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 6 letras: ")
    print(palavras_6)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 7 letras: ")
    print(palavras_7)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 8 letras: ")
    print(palavras_8)
    print("---------------------------------------------------------------------------------")
    print("Palavras de 9 letras: ")
    print(palavras_9)
    print("---------------------------------------------------------------------------------")
    print("Palavras de muitas muitas letras: ")
    print(palavras_10)
    print("---------------------------------------------------------------------------------")

imprime_tudo()