#Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
print("Inicio do programa")

contagem_numero = 0
soma_numeros=0

while True:
    numero=int(input("Digite um número: "))
    if numero == 0:
        print(f"Você digitou {contagem_numero} números")
        print(f"A soma dos números digitados é {soma_numeros}")
        print(f"A média dos números digitados é {soma_numeros/contagem_numero}")
        print("Fim do programa")
        break
    else:
        contagem_numero = contagem_numero + 1
        soma_numeros = soma_numeros + numero 
        