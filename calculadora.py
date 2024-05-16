#Calculadora Simples by George Telles

while True:
    operacao = input("Qual operação deseja realizar? \n+ Soma\n- Subtração\n/ Divisão\n* Multiplicação\n")

    if operacao == "+":
        numero1 = float(input("Insira o numero 1: "))
        numero2 = float(input("Insira o numero 2: "))
        resultado_soma = numero1 + numero2
        print(f"O resultado da soma é {resultado_soma}")
    elif operacao == "-":
        numero1 = float(input("Insira o numero 1: "))
        numero2 = float(input("Insira o numero 2: "))
        resultado_subtraçao = numero1 - numero2
        print(f"O resultado da subtração é {resultado_subtraçao}")
    elif operacao == "/":
        numero1 = float(input("Insira o numero 1: "))
        numero2 = float(input("Insira o numero 2: "))
        resultado_divisao = numero1 / numero2
        print(f"O resultado da soma é {resultado_divisao}")
    elif operacao == "*":
        numero1 = float(input("Insira o numero 1: "))
        numero2 = float(input("Insira o numero 2: "))
        resultado_multiplicacao = numero1 * numero2
        print(f"O resultado da soma é {resultado_multiplicacao}")
    
    x = input("Deseja fazer outra operação?\nSim\nNão\n")
    if x == "Sim":
        continue
    else:
        break
