print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")
 
idade = int(input("Digite sua idade: "))
if idade >= 19:
    print(nome, "é maior de idade.")
else:
    print(nome, "é menor de idade.")