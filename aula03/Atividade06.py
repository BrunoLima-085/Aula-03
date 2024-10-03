soma = 0

while True:
    
    numero = float(input("\nDigite um número (digite um número negativo para encerrar): "))
    
    if numero < 0:
        break
    
    soma += numero

print(f"\nA soma dos números positivos é: {soma}")