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

# Crie variáveis com informações do seu dia:

nome = "Daniel"
idade = 45
numero_filhos = 2
cidade = "São Vicente"
print(nome, idade, numero_filhos, cidade)


# 2. Troca de valores:

idade = 72
numero_filhos = 2
temp = idade
idade = numero_filhos
numero_filhos = temp
print(idade, numero_filhos)

#  3. Exercício “Lista de Compras”:

produto1 = "Leite"
produto2 = "Pão"
quantidade1 = 12
quantidade2 = 30
print("Lista:", produto1, quantidade1, produto2, quantidade2)

#  4. Calculando total do mercado:

preco_leite = 5.89
preco_pao = 1.10
quantidade_leite = 12
quantidade_pao = 6
total = (preco_leite * quantidade_leite) + (preco_pao * quantidade_pao)
print("Total da compra:", total)

#  5. Misture tipos de dados (texto, número, booleano):

nome_filho = "Nickolas"
idade_filho = 8
gosta_brinquedo = True
print(nome_filho, idade_filho, gosta_brinquedo)

# Crie uma variável para seu prato favorito.

prato_favorito = "Salmão no forno com alcaparras na manteiga"
tempo_de_preparo = 40
print("Meu prato favorito é:", prato_favorito)
print("Tempo de preparo:", tempo_de_preparo, "minutos")
print(f"Meu prato favorito é {prato_favorito} e o tempo de preparo é {tempo_de_preparo} minutos.")

# Crie uma variável para a quantidade de horas dormidas ontem.

horas_dormidas_ontem = 6
print("Quantas horas dormi ontem?", horas_dormidas_ontem)
print(f"Quantas horas eu dormi ontem? {horas_dormidas_ontem}")

# Crie uma variável booleana (True/False) dizendo se você já tomou café hoje.

tomou_cafe_hoje = True
resposta = "Sim" if tomou_cafe_hoje else "Não"
print(f"Você já tomou café hoje? {resposta}")


# Crie três variáveis para os nomes das pessoas da sua casa e imprima tudo junto.

moradores = ["Daniel", "Thatiana", "Alicia", "Nickolas", "Eliane"]
print(f"Quem são os moradores? {', '.join(moradores)}")


# 7. Explique para você mesma: O que é uma variável? é o nome que se dá a um valor para a memoria do computador ou melhor dizendo:  Uma variável é um nome que damos para guardar um valor na memória do computador. Assim, sempre que usamos esse nome no código, estamos nos referindo a esse valor guardado.

# 8. Qual a diferença entre um número inteiro (int), um número decimal (float) e um texto (str) no Python? É que o numero inteiro é para um exemplo a idade de uma pessoa é inteiro, o float é o decimal no caso de altura de uma pessoa e o str string para um texto no caso um nome ou para deixar mais didático: int (número inteiro): É um número sem casas decimais. Exemplo: a idade de uma pessoa (ex: idade = 42)float (número decimal):É um número que pode ter casas decimais. Exemplo: altura de uma pessoa (ex: altura = 1.61)str (texto ou string):É uma sequência de caracteres, usado para textos. Exemplo: o nome de uma pessoa (ex: nome = "Thatiana") Resumindo: int: para números inteiros (ex: 1, 42, -5) float: para números decimais (ex: 3.14, 1.61) str: para textos (ex: "Thatiana", "Olá Mundo")

# 9. O que acontece se você tentar somar uma variável de texto com um número? eu coloco print(nome + str(numero)), pois quando é texto e numero eu tenho que colocar o str para poder aparecer em modo texto e numero ou melhor dizendo didaticamente: Eu coloco print(nome + str(numero)), pois quando é texto e número eu tenho que colocar o str para poder aparecer em modo texto e número. pois em python para juntar texto com número, o número precisa ser convertido para texto usando str(). Se não fizer isso, vai dar erro de tipo.

# 10. Crie variáveis para os horários das refeições das crianças.

# Horários das refeições das crianças
hora_cafe_manha = "7:30"
hora_almoco = "12:00"
hora_lanche_tarde = "15:30"
hora_jantar = "19:00"

print("Horário do cafe da manhã:", hora_cafe_manha)
print("Horário do almoço:", hora_almoco)
print("Horário do lanche da tarde:", hora_lanche_tarde)
print("Horário do jantar:", hora_jantar)

# exercicio com a função imbutida o f-string
cafe_da_manha = "8:00"
almoco = "12:30"
lanche_da_tarde = "16:00"
jantar = "19:30"

print(f"Horários das refeições das crianças:")
print(f"Café da manhã: {cafe_da_manha}")
print(f"Almoço: {almoco}")
print(f"Lanche da tarde: {lanche_da_tarde}")
print(f"Jantar: {jantar}")

print(f"Cafe da manhã: {cafe_da_manha} | Almoço: {almoco} | Lanche: {lanche_da_tarde} | Jantar: {jantar} ")

#ou modo multitarefas

refeicoes = ["8:00", "12:30", "16:00", "19:30"]

print("Horários das refeições das crianças:")
print(f"Café da manhã: {refeicoes[0]}")
print(f"Almoço: {refeicoes[1]}")
print(f"Lanche da tarde: {refeicoes[2]}")
print(f"Jantar: {refeicoes[3]}")

#ou para imprimir tudo de uma vez 
nomes_refeicoes = ["Café da manhã", "Almoço", "Lanche da tarde", "Jantar"]
horarios = ["8:00", "12:30", "16:00", "19:30"]

for nome, horario in zip(nomes_refeicoes, horarios):
    print(f"{nome}: {horario}")










