# Condicionais -> if, else
idade = 18

# estrutura do if => if COMPARACAO:

# o bloco do if, só executado se a ccond. for verdadeira

if idade > 18:
    print("Você é maior de idade")

# else
# é execcutado em casos onde o if não executa

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é Menor de idade")

# meia entrada => menor de 18 anos Ou esteja estudando em esola publia / fauldade

estuda_rede_publica = False

if idade < 18 or estuda_rede_publica:
    print("Tem direito a meia entrada")

    # nota: A, B C
    # > 9 = A, > 8 = b, > 6 = C

    nota = 6.5

    # elife => else if
    # uma condicao intermediaria entre if e else

    if nota > 9:
        print("O seu conceito é A")
    elif nota > 8:
        print("O seu conceito é B")
    elif nota > 6:
        print("O seu conceito é C")
    else:
        print("Você deve melhorar sua nota...")


# climas: ensolarado, chuvoso, nublado

clima = "ensolarado"

if clima == "ensolarado":
    print("Vista uma camiseta e shorts.")
elif clima == "nublado":
    print("Leve uma jaqueta leve.")
elif clima == "chuvoso":
    print("Não esqueça o guarda-chuva.")
else:
    print("verifique a previsão do tempo.")


# comissao de vendas
# > 1000 = .5%
# > 500 = 1%
# = 2%

venda = 1200

if venda > 1000:
    comissao = venda * 0.005
    print("A comissão da venda foi: ", comissao)
elif venda > 500:
    comissao = venda * 0.01
    print("A comissão da venda foi: ", comissao)
else:
    comissao = venda * 0.02
    print("A comissão da venda foi: ", comissao)

# baseado numa entrada do usuario se o numero é maior ou menor que zero
# funcao input

numero = float(input("Digite um número: "))

if numero > 0:
    print("O numero é maior que 0", numero)

else:
    print("O numero é maior que 0", numero)


# if condicao:
# bloco de código a ser executado se a condicao for verdadeira 

idade = 18

if idade >= 18:
    print("Você é maior de idade.")



# if condicao:
# bloco de código a ser executado se a condicao for verdadeira 
# else: é o bloco do código se a condição for falsa 


idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# if condicao1:
# bloco de código a ser executado se a condicao for verdadeira 
# elif condicao2: é o bloco de código se a condicao2 for verdadeira 
# elif condicao3: será o bloco de codigo se a condicao3 for verdadeira 
# else: é o bloco do código se todas essas outras condições anteriores forem falsa

nota = 85

if nota >= 90:
    print("Sua nota é A.")
elif nota >= 80:
    print("Sua nota é B.")
elif nota >= 70:
    print("Sua nota é C.")
else:
    print("Você precisa melhorar.")



# Ao dirigir você reage de acordo com o semáforo

semaforo = "vermelho"

if semaforo == "verde":
    print("Siga em frente.")
elif semaforo == "Amarelo":
    print("Prepare-se para parar.")
elif semaforo == "vermelho":
    print("Pare o veículo.")
else:
    print("Sinal desconhecido, proceda com cautela..")
    

# Calculando desconto de compras: : Uma loja oferece descontos com base no valor da compra.
# Se o valor for maior ou igual a R$1000, o desconto é de 10%.
# Se for entre R$500 e R$999, o desconto é de 5%.
# Caso contrário, não há desconto

valor_compra = 750

if valor_compra >= 1000:
    desconto = valor_compra *0.05
    print("Você recebeu um desconto de 10%. Valor do desconto: R$", desconto)

elif valor_compra >= 500:
    desconto = valor_compra *0.10
    print("Você recebeu um desconto de 5%. Valor do desconto: R$", desconto)

else:
    desconto = 0
    print("Não há desconto disponível.")

valor_final = valor_compra - desconto
print("Valor final da compra: R$", valor_final)


# Você quer fazer um passeio ao parque, mas depende do clima e do dia da semana.
# Se for fim de semana (sábado ou domingo) e não estiver chovendo, você vai ao parque.
# Caso contrário, fica em casa e assiste a um filme

dia_da_semana = "sábado"
chovendo = False

if (dia_da_semana == "sábado" or dia_da_semana == "domingo") and not chovendo:
    print("Ótimo dia para ir ao parque!")
else:
    print("Vamos ficar em casa e assistir a um filme.")


# 1. Verificando Se um Número é Positivo, Negativo ou Zero
# Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo ou zero.


numero = float(input("Digite um número: "))

if numero > 0:
    print("O numero é positivo.")
elif numero < 0:
    print("O numero é negativo.")
else:
    print("O numero é zero.")


# 2. Calculadora Simples
# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza o cálculo correspondente.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Erro: Divisão por zero!")
else: 
    print("Operação inválida.")



# Classificação de Idade
# Crie um programa que classifica a idade de uma pessoa em:
# Criança: 0 a 12 anos
# Adolescente: 13 a 17 anos
# Adulto: 18 a 59 anos
# Idoso: 60 anos ou mais

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
elif idade >= 60:
    print("Você é um idoso.")
else:
    print("Idade inválida.")


# Verificando Ano Bissexto
# Crie um programa que verifica se um ano é bissexto.
# Um ano é bissexto se for divisível por 4.
# Mas não é bissexto se for divisível por 100, exceto se for divisível por 400

ano = int(input ("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")



# Simulador de Caixa Eletrônico
# Crie um programa que simula um caixa eletrônico. O usuário deve informar o valor do saque
# (apenas valores inteiros) e o programa deve informar quantas cédulas de cada valor serão fornecidas.
# Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.

valor_saque = int(input("Digite o valor do saque: R$"))

if valor_saque <= 0:
    print("Valor inválido.")
    
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100
    
    cedulas_50 = valor_saque // 50
    valor_saque %= 50
    
    cedulas_20 = valor_saque // 20
    valor_saque %= 20
    
    cedulas_10 = valor_saque // 10
    valor_saque %= 10
    
    cedulas_5 = valor_saque // 5
    valor_saque %= 5
    
    cedulas_2 = valor_saque // 2
    valor_saque %= 2
    
    if valor_saque != 0:
        print("Não é possível sacar o valor especificado com as cédulas disponíveis.")
        
    else:
        print("Cédulas entregues:")
        if cedulas_100 > 0:
            print(f"{cedulas_100} x R$100")
        if cedulas_100 > 0:
            print(f"{cedulas_50} x R$50")
        if cedulas_100 > 0:
            print(f"{cedulas_20} x R$20")
        if cedulas_100 > 0:
            print(f"{cedulas_10} x R$10")
        if cedulas_100 > 0:
            print(f"{cedulas_5} x R$5")
        if cedulas_100 > 0:
            print(f"{cedulas_2} x R$2")
    
    
# Aprovando Empréstimo Bancário
# Crie um programa para uma instituição bancária que analisa o pedido de empréstimo.
# O cliente deve informar o valor do empréstimo, a renda mensal e o número de parcelas.
# O empréstimo será aprovado se o valor da parcela não exceder 30% da renda mensal.

valor_emprestimo = float(input("Digite o valor do empréstimo: R$"))
renda_mensal = float(input("Digite sua renda mensal: R$"))
numero_parcelas = int(input("Digite o número de parcelas: "))

valor_parcela = valor_emprestimo / numero_parcelas
limite_parcelas = renda_mensal * 0.30

if valor_parcela <= limite_parcelas:
    print("Emprestimo aprovado.")
    print(f"Valor da parcela: R${valor_parcela:.2f}")
else:
    print("Emprestimo negado.")
    print(f"Valor da parcela R${valor_parcela:.2f} excede 30% da renda mensal.")
    
    
# Jogo Pedra, Papel ou Tesoura
# Crie um programa que simula o jogo "Pedra, Papel ou Tesoura" entre o usuário e o computador.
    
    
import random

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu: {usuario}")
print(f"O ccomputador escolheu: {computador}")

if usuario == computador:
    print("Empate!")
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "papel" and computador == "pedra") or \
     (usuario == "tesoura" and computador == "papel"):
    print("Você venceu!")
elif usuario in opcoes:
    print("Você perdeu")
else:
    print("Escolha inválida.")
    
    
    
# Calculadora de Tarifas de Táxi
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro rodado. Crie um programa que calcula o valor total da corrida com base na distância percorrida.
    

distancia = float(input("Digite a distância percorrida em km: "))

tarifa_basica = 4.00
custo_por_km = 0.25

valor_total = tarifa_basica + (custo_por_km * distancia)

print(f"Valor total da corrida: R${valor_total:.2f}")
