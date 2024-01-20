from collections import Counter

def separar_digitos_individuais(numero):
    # Converte o número em uma string
    str_numero = str(numero)

    # Itera sobre os dígitos da string e converte cada um para um número 
    for digito in str_numero:
        vetor_saida.append(int(digito))

def extrair_digitos_sem_zeros_finais(numero):
    str_numero = str(numero)
    str_sem_zeros_finais = str_numero.rstrip('0')
    
    numero_sem_zeros_finais = int(str_sem_zeros_finais)
    
    return numero_sem_zeros_finais

def remover_primeiro_digito(numero):
    str_numero = str(numero)
    str_sem_primeiro_digito = str_numero[1:]
    
    primeiro_digito = str_numero[0]
    numero_sem_primeiro_digito = int(str_sem_primeiro_digito)
   
    numero_apenas_primeiro_digito = int(primeiro_digito)
    
    return numero_sem_primeiro_digito, numero_apenas_primeiro_digito

def comparar_primeiros_digitos(numero1, numero2):
    str_numero1 = str(numero1)
    str_numero2 = str(numero2)

    digitos1 = str_numero1[0]
    digitos2 = str_numero2[0]

    if digitos1 == digitos2:
        return True
    else:
        return False

def contar_frequencia_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            frequencia_caracteres = Counter(conteudo)
            tamanho = arquivo.tell()
            return frequencia_caracteres, tamanho
    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_do_arquivo = 'teste.txt'
frequencia, tamanho = contar_frequencia_arquivo(nome_do_arquivo)
caracteres = frequencia.items()
frequencia_carac = []
caracteres_lidos = []
probabilidade_carac = []
acumulada = []

for caractere, frequencia in caracteres:
    caracteres_lidos.append(caractere)
    frequencia_carac.append(frequencia)
    probabilidade_carac.append(frequencia/tamanho)

aux = caracteres_lidos[4]
caracteres_lidos[4] = caracteres_lidos[3]
caracteres_lidos[3] = aux

indices = len(caracteres_lidos)
acumulada.append(0)
acumulada.append(probabilidade_carac[0])

for i in range (1,6,1):
    acumulada[i] = acumulada[i-1]+probabilidade_carac[i-1]
    acumulada.append(acumulada[i])
acumulada = acumulada[:-1]

with open("teste.txt", 'r', encoding='utf-8') as arquivo:
    # Ler o conteúdo do arquivo
    vetor_saida = []
    low = 0
    high = 9999
    print(low, high)
    caracter = arquivo.read(1)
    print(caracter)
    for i in range (0,5,1):
        if caracter == caracteres_lidos[i]:
            new_low = low + (high-low+1) * acumulada[i]
            new_low = int(new_low)
            new_high = low + (high-low+1) * acumulada[i+1] - 1
            new_high = int(new_high)
            print(new_low, new_high)
        else:
            continue
    while caracter:
        caracter = arquivo.read(1)
        while comparar_primeiros_digitos(new_low, new_high):
            new_low, saida = remover_primeiro_digito(new_low)
            new_high, saida = remover_primeiro_digito(new_high)
            vetor_saida.append(saida)
            new_low = new_low * 10
            new_high = new_high * 10 + 9
            print(new_low, new_high)
        for i in range (0,5,1):
            if caracter == caracteres_lidos[i]:
                print(caracter)
                original_new_low = new_low
                new_low = new_low + ((new_high-new_low+1) * acumulada[i])
                new_low = int(new_low)
                new_high = original_new_low + ((new_high-original_new_low+1) * acumulada[i+1]) - 1
                new_high = int(new_high)
                print(acumulada[i], acumulada[i+1])
                print(new_low, new_high)
            else:
                continue
    
    ultimo_new_low_sem_zeros = extrair_digitos_sem_zeros_finais(new_low)
    separar_digitos_individuais(ultimo_new_low_sem_zeros)

print(vetor_saida)