# Adição
a = 10
b = 5
soma = a + b # 15
# Subtração
diferenca = a - b # 5
# Multiplicação
produto = a * b # 50
# Divisão
divisao = a / b # 2.0
# Módulo
resto = a % b # 0
# Exponenciação
potencia = a ** b # 100000
# Divisão Inteira
div_inteira = a // b # 2



x = 10
y = 5
# Igual a
print(x == y) # False
# Diferente de
print(x != y) # True
# Maior que
print(x > y) # True
# Menor que
print(x < y) # False
# Maior ou igual a
print(x >= 10) # True
# Menor ou igual a
print(y <= 5) # True



idade = 20
possui_carteira = True
# Verificar se pode alugar um carro
pode_alugar = (idade >= 21) and possui_carteira
print("Pode alugar o carro?", pode_alugar) # False
# Verificar se tem direito a meia-entrada
estudante = False
idoso = idade >= 60
meia_entrada = estudante or idoso
print("Tem direito a meia-entrada?", meia_entrada) # False
# Inverter uma condição
chovendo = False
nao_chovendo = not chovendo
print("Está chovendo?", chovendo) # False
print("Não está chovendo?", nao_chovendo) # True




# Preços dos itens
pao = 3.50
leite = 4.20
cafe = 2.80
# Total da compra
total_compra = pao + leite + cafe
# Valor pago
valor_pago = 20.00
# Calcular troco
troco = valor_pago - total_compra
print("Total da compra: R$", total_compra)
print("Troco a receber: R$", troco)



# Dados do estudante
nota_media = 8.5
frequencia = 80
# Verificar aprovação
aprovado = (nota_media >= 7.0) and (frequencia >= 75)
print("Estudante aprovado?", aprovado) # True


# Dados da compra
quantidade_itens = 8
valor_total = 120.00
# Verificar desconto
desconto = (quantidade_itens > 10) or (valor_total > 100)
print("Cliente tem direito ao desconto?", desconto) # True



# Dados do usuário
senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False
# Verificar acesso
acesso_concedido = (senha_inserida == senha_correta) and not
usuario_bloqueado
print("Acesso concedido?", acesso_concedido) # True



# Valor total da conta
conta = 150.00
# Número de amigos
amigos = 3
# Valor por pessoa
valor_por_pessoa = conta / amigos
# Verificar se a divisão é exata
divisao_exata = (conta % amigos) == 0
print("Cada um deve pagar: R$", valor_por_pessoa)
print("A divisão é exata?", divisao_exata) # True



# Solicitar idade
idade = int(input("Digite sua idade: "))
# Verificar permissão
pode_assistir = idade >= 16
print("Pode assistir ao filme?", pode_assistir)




# Solicitar peso e altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
# Calcular IMC
imc = peso / (altura ** 2)
# Verificar peso ideal
peso_ideal = (imc >= 18.5) and (imc <= 24.9)
print("Seu IMC é:", imc)
print("Você está no peso ideal?", peso_ideal)



# Solicitar número
numero = int(input("Digite um número inteiro: "))
# Verificar se é par ou ímpar
eh_par = (numero % 2) == 0
print("O número é par?", eh_par)






# Calculando troco
pao = 3.50
leite = 4.20
cafe = 2.80

total_compra = pao + leite + cafe

valor_pago = 20

troco = valor_pago - total_compra

print("Valor pago: R$", valor_pago)
print("Seu troco será de: R$", troco)


# Verificando prova do Enem 

# Aprovado se nota >= 7  e frequencia >= 75% 
nota = 7
frequencia = 75

aprovado = (nota >= 7) and (frequencia >= 75)
print("Aluno esta aprovado: ", aprovado)


# Oferta especial
# Desconto se comprar mais 10 itens OU comprar acima de 100

qtd_itens = 11
valor_total = 90

direito_desconto = (qtd_itens > 10) or (valor_total > 100)
print("Cliente tem direito ao desconto: ", direito_desconto)

# Acesso ao sistema
# senha correta E não pode estar bloqueado

senha_inserida = "abcd1234"
senha_correta = "abcd1234"
bloqueado = False

acesso_permitido = (senha_inserida == senha_correta) and (bloqueado == False)
print("Usuario pode acessar o destino? ", acesso_permitido)

# Divisão de Tarefas

conta = 150
amigos = 3

divisao_conta = conta / amigos 
resto_divisao = (conta % amigos) == 0
print("Valor divido para os 3 será de RS", divisao_conta)
print("Divisão foi exata sem resto ? ", resto_divisao)

# Classe etária
idade = int(input("Digite sua idade: "))

permitido = idade >= 16

print("Você pode assitir o filme? ", permitido)

# Calculadora de IMC
peso = float(input("Digite seu Peso em KG: "))
altura = float(input("Digite sua Altura em metros: "))

massa_corporal = peso / (altura ** 2)
peso_ideal = (massa_corporal >= 18.5) and (massa_corporal <= 24.9)

print("Seu IMC é: ", massa_corporal)
print("Estou no peso ideal? ", peso_ideal)

# par ou impar
numero = int(input("Insira um numero: "))

par = (numero % 2) == 0 

print("Meu numero é par: ", par)
# Entrada de dados
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado
print(f"Seu IMC é {imc:.2f}")


# Entrada de dados
try:
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser valores positivos.")
    else:
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        print(f"\nSeu IMC é {imc:.2f}\n")

        # Peso ideal: IMC entre 18.5 e 24.9
        peso_minimo_ideal = 18.5 * (altura ** 2)
        peso_maximo_ideal = 24.9 * (altura ** 2)

        # Classificação do IMC e análise de peso
        if imc < 18.5:
            print("⚠️ Você está abaixo do peso.")
            print(f"Para atingir o peso ideal, você precisa ganhar pelo menos {(peso_minimo_ideal - peso):.2f} kg.")
        elif 18.5 <= imc <= 24.9:
            print("✅ Parabéns! Você está no peso ideal.")
        elif 25 <= imc <= 29.9:
            print("⚠️ Você está com sobrepeso.")
            print(f"Para atingir o peso ideal, você precisa perder pelo menos {(peso - peso_maximo_ideal):.2f} kg.")
        elif 30 <= imc <= 34.9:
            print("❗ Obesidade grau I.")
            print(f"Para atingir o peso ideal, você precisa perder pelo menos {(peso - peso_maximo_ideal):.2f} kg.")
        elif 35 <= imc <= 39.9:
            print("❗❗ Obesidade grau II.")
            print(f"Para atingir o peso ideal, você precisa perder pelo menos {(peso - peso_maximo_ideal):.2f} kg.")
        else:
            print("🚨 Obesidade grau III (mórbida).")
            print(f"Para atingir o peso ideal, você precisa perder pelo menos {(peso - peso_maximo_ideal):.2f} kg.")

        # Exibição do intervalo de peso ideal
        print(f"\n💪 Seu peso ideal está entre {peso_minimo_ideal:.2f} kg e {peso_maximo_ideal:.2f} kg.")
except ValueError:
    print("❌ Por favor, insira valores numéricos válidos.")
    
    

