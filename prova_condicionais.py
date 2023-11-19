#Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade= int(input("Qual a velocidade do carro? "))

if velocidade > 80:
    excesso = velocidade - 80
    print(f"Você ultrapassou o limite de velocidade e precisa pagar uma multa de R$ {20*excesso}.")
else:
    print("Você está no limite de velocidade, parabéns!")