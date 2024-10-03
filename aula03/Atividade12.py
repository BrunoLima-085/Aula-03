senha = "1234"
chute = ""

while chute != senha:
    chute = input("Digite a senha: ")
    if chute == senha:
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")