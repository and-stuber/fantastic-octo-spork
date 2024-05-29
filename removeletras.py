letras_permitidas = ["a", "u", "o", "d", "ç", "r", "o", "p"]
array_letras_portugues = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']

###############################################################

letras_a_remover = letras_permitidas

def remover_letras(letras_a_remover, array_letras):
    for letra in letras_a_remover:
        if letra in array_letras:
            array_letras.remove(letra)
    return array_letras

array_sem_letras = remover_letras(letras_a_remover, array_letras_portugues)

print(array_sem_letras)