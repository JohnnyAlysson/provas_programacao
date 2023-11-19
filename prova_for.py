#[LP-A03] Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. 

tabuada= int(input("Qual tabuada você deseja: "))

for i in range(1,11):

    print(f" {i} x {tabuada} = {tabuada*i} ")