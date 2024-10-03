def tab():
    
    soma = 0
    contador = 1

    while soma <= 50:
        soma += contador
        print(f"Soma atual: {soma}")
        contador += 1

    print(f"\nSoma final: {soma}")

tab()
