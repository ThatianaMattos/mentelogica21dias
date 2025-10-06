# estrutura de repetição

# repetir N vezes
# onde n, a gente pode definir
# ou n é uma condição

# array é sempre em conchetes[]

frutas = ["maçã", "banana", "laranja"]

# for item_individual in lista:
#   bloco repetido N vezes

for fruta in frutas:
    print("Fruta: ", fruta)

for fruta in frutas:
    print("Eu gosto de", fruta)

for i in range(5):
    print("Num: ", i)

print(frutas[0])
print(frutas[1])


# while

contador = 0

while contador < 5:
    print("Num while:", contador)
    contador += 1

# um loop com uma condicao mal definida = loop infinito = bug

for i in range(10):
    if i == 5:
        break

    print("Num for", i)


# break => para o loop
# continue => pula uma execucao

for n in range(10):
    if i == 2:
        continue
    print("For in continue", i)


# calcular a multiplicacao de 1 a N
N = int(input("Digite um numero "))
multiplicacao = 0

for i in range(1, N + 1):
    resultado = N * i
    print(resultado)

# identificar numeros pares e impares até 20
pares = 0
impares = 0

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

    print("Pares: ", pares)
    print("Impares: ", impares)


# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 a N.

N = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, N + 1):
    soma += i  # Equivale a soma = soma + i

print("A soma dos números de 1 a", N, "é:", soma)

# Tabuada de um Número

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# Contando Números Pares e Ímpares

pares = 0
impares = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

# Adivinhe o Número

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
        
# Calculando Fatorial de um Número

N = int(input("Digite um número inteiro positivo: "))

fatorial = 1

if N < 0:
    print("Não existe fatorial de número negativo.")
elif N == 0 or N == 1:
    print(f"O fatorial de {N} é 1.")
else:
    for i in range(1, N+1):
        fatorial *= i
    print(f"O fatorial de {N} é {fatorial}.")
    
    
#  Série Fibonacci Exiba os primeiros N termos da série de Fibonacci.
# ● A série de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores.
# ● Exemplo: 0, 1, 1, 2, 3, 5, 8, 13...

N = int(input("Quantos termos da série Fibonacci você quer ver? "))

termo1 = 0
termo2 = 1
contador = 0

if N <= 0:
    print("Por favor, insira um número positivo.")
elif N == 1:
    print("Série Fibonacci até", N, "termo:")
    print(termo1)
else:
    print("Série Fibonacci:")
    while contador < N:
        print(termo1)
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1
        

#  Jogo da Forca Simples
# Crie um jogo da forca simples em que o usuário deve adivinhar uma palavra letra por letra

palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    print(("Palavras:", " ".join(letras_descobertas)))
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
            print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")
if "_" not in letras_descobertas:
    print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
