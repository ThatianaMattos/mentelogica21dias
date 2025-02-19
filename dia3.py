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

