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
