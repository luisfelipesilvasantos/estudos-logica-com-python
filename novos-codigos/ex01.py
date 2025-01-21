# Neste algoritmo em Python, ele cria uma lista de números, calcula a soma e a média, e identifica o maior número na lista.

# Declaração de variáveis e inicialização de uma lista
numeros = [10, 20, 30, 40, 50]  # Lista de números
soma = 0  # Variável para armazenar a soma dos números
maior_numero = numeros[0]  # Assumimos que o primeiro número é o maior inicialmente

# Iteração para calcular a soma e encontrar o maior número
for numero in numeros:
    soma += numero  # Adiciona o número atual à soma
    if numero > maior_numero:  # Verifica se o número atual é maior que o maior encontrado até agora
        maior_numero = numero

# Cálculo da média
media = soma / len(numeros)

# Exibição dos resultados
print("Lista de números:", numeros)
print("Soma dos números:", soma)
print("Média dos números:", media)
print("Maior número da lista:", maior_numero)
