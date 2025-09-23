# Preços dos itens
frango = 28.50
carne = 69.90
ovo = 38.60

# Total da compra
total_compra = frango + carne + ovo

#  Valor pago
valor_pago = 150.00

# Calcular troco
troco = valor_pago - total_compra

print("Total da compra: R$", total_compra)
print("Troco a receber: R$", troco)


# Verificando Aprovação de um Exame
nota_media = 8.5
frequencia = 80

# Verificar aprovação
aprovado = (nota_media >= 7.0) and (frequencia >=75)

print("Estudante aprovado?", aprovado) # True

# Oferta Especial Oferta 
qtd_itens = 12
valor_total = 120

# Verificar direito a desconto
direito_desconto = (qtd_itens > 10) or (valor_total > 100)
print("Cliente tem direito a desconto?", direito_desconto) # True

# itens exercicio 1

pao = 3.50
leite = 4.20
cafe = 2.80

# somar o total da compra 

total = pao + leite + cafe

# definindo o valor pago

valor_pago = 20.00

# calcular troco

troco = valor_pago - total

# exibir o resultado 

print("Total da compra: R$", total)
print("Valor pago: R$", valor_pago)
print("Troco: R$", troco)


print(f"Total da compra: R$ {total:.2f}")
print(f"Valor pago: R$ {valor_pago:.2f}")
print(f"Troco: R$ {troco:.2f}")


# Verificando Aprovação em um Exame

nota = 8.5
frequencia = 80

nota_minima = 7.0
frequencia_minima = 75
if nota >= nota_minima and frequencia >= frequencia_minima:
    print ("Aluno aprovado!")
else:
    print("Aluno reprovado!")









    # nota > 7 e frequencia > 80%

    nota = 8
    frequencia = 60

    passou_de_ano = (nota>7) and (frequencia > 80)

    print("Passou de ano: ", passou_de_ano)


    # senhas iguais 
    # criando um registro de usuario

    senha = "teste123"
    confirmacao_senha = "teste1234"

    aviso_senha_errada = senha != confirmacao_senha

    print("A senha não combina? ", aviso_senha_errada)


# mesa de bar
# 123.85
# quanto cada pessoa vai pagar? 3

conta = 123.85
pessoas = 3

parte_de_cada_um = conta / pessoas

print("Cada um tem que pagar: ", parte_de_cada_um)








