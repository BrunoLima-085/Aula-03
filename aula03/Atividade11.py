def numeros():

    while True:
        try:
            numero = int(input("Digite um número entre 1 e 10: "))

            if numero <= 1 or numero <= 10:
             print("\nNúmero válido!")
             break
            else:
              print("\nNúmero inválido. Tente novamente!")
            
        except ValueError:
            print("Digite um número válido!")

        

numeros()