print("Bem vindo a calculadora de operções basicas!")
print("Digite o numero referente a operação desejada:")
print("1:Soma \n2:Subtração \n3:Multiplicação \n4:Divisão")
operacao = str(input("Operação: "))
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if operacao == "1":
    resultado = numero1 + numero2
    print(str(numero1) + "+" + str(numero2) + "=" + str(resultado))

if operacao == "2":
    resultado = numero1 - numero2
    print(str(numero1) + "-" + str(numero2) + "=" + str(resultado))

if operacao == "3":
    resultado = numero1 * numero2
    print(str(numero1) + "x" + str(numero2) + "=" + str(resultado))

if operacao == "4":
    resultado = numero1 / numero2
    print(str(numero1) + "/" + str(numero2) + "=" + str(resultado))
