def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        return a / b if b != 0 else "Erro! Divisão por zero"
    else:
        return "Operação inválida"

# Primeira calculadora
print("=== Primeira Calculadora ===")
try:
    num1_1 = float(input("Digite o primeiro número: "))
    num1_2 = float(input("Digite o segundo número: "))
    operacao1 = input("Escolha a operação (+, -, *, /): ")
    resultado1 = calculadora(num1_1, num1_2, operacao1)
    
    if isinstance(resultado1, str):
        print(f"Erro: {resultado1}")
        exit()

except ValueError:
    print("Erro! Entrada inválida.")
    exit()

print(f"Resultado da primeira calculadora: {resultado1}")

# Segunda calculadora
print("\n=== Segunda Calculadora ===")
try:
    num2_1 = float(input("Digite o primeiro número: "))
    num2_2 = float(input("Digite o segundo número: "))
    operacao2 = input("Escolha a operação (+, -, *, /): ")
    resultado2 = calculadora(num2_1, num2_2, operacao2)
    
    if isinstance(resultado2, str):
        print(f"Erro: {resultado2}")
        exit()

except ValueError:
    print("Erro! Entrada inválida.")
    exit()

print(f"Resultado da segunda calculadora: {resultado2}")

# Cálculo final usando os dois resultados
if isinstance(resultado1, (int, float)) and isinstance(resultado2, (int, float)):
    print("\n=== Cálculo Final ===")
    operacao_final = input("Escolha a operação final entre os dois resultados (+, -, *, /): ")
    resultado_final = calculadora(resultado1, resultado2, operacao_final)
    print(f"Resultado final: {resultado_final}")
else:
    print("\nErro! Um dos cálculos anteriores não é válido para continuação.")