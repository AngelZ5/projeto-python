print("Sistema de verificação de idade")
nome = input("Digite seu nome: ")#o usuário deve inserir seu nome
 
idade = int(input("Digite sua idade: "))#o usuário deve inserir sua idade
if idade >= 18:#se o usuário tiver 18 anos ou mais, ele é maior de idade
    print(nome, "é maior de idade.")
elif idade >=14:#se o usuário tiver 14 anos ou mais, ele é adolescente
    print(nome, "é adolescente.")
else:#se o usuário tiver menos de 14 anos, ele é menor de idade
    print(nome, "é menor de idade.")