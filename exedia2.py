idade = 43
nome = "Thatiana"
altura = 1.41
estudante = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudante:", estudante)

ano_nascimento = 2025 - idade
print("Ano de Nascimento:", ano_nascimento)
maior_de_idade = idade>=18
print("Maior de idade:", maior_de_idade)

frase = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos." 
print(frase)

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("A temperatura em Fahrenheit é:", fahrenheit)

raio = float(input("Digite o raio do círculo: "))
pi = 3.14159
area = pi * raio ** 2
print("A área do círculo é:", area)





