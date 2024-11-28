# soma.py com verificação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 < 0 or num2 < 0:
    print("Pelo menos um número é negativo.")
else:
    soma = num1 + num2
    print("A soma dos números é:", soma)
