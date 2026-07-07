print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")
 
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print(nome, "é maior de idade.")
elif idade >=14:
    print(nome, "é adolescente.")
else:
    print(nome, "é menor de idade.")