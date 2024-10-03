def tab_mult_3():

    num = int(input("Digite um número para ver sua tabuada: "))
    contador = 1

    while contador <= 10:
        resultado = num + contador

        if resultado % 3 == 0:
            print(f"{num} + {contador} = {resultado}")
        
        contador += 1

tab_mult_3()
