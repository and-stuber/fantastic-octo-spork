import unidecode

def results_to_unicode():
  # Caminho para o seu arquivo com palavras
  arquivo_entrada = './data/palavras_new.txt'
  arquivo_saida = './data/palavras_new_unicode.txt'
  
  # Ler as palavras do arquivo de entrada
  with open(arquivo_entrada, 'r', encoding='utf-8') as f:
      palavras = f.readlines()

  # Remover acentos das palavras
  palavras_sem_acento = [unidecode.unidecode(palavra.strip()) for palavra in palavras]

  # Gravar as palavras sem acento no arquivo de saída
  with open(arquivo_saida, 'w', encoding='utf-8') as f:
      for palavra in palavras_sem_acento:
          f.write(palavra + '\n')

  print("As palavras foram processadas e salvas em", arquivo_saida)
  