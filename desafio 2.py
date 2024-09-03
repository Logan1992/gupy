def is_fibonacci_number(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

numero_informado = int(input("Digite um número:"))

if is_fibonacci_number(numero_informado):
    mensagem = f"O número {numero_informado} pertence à sequência de Fibonacci."
else:
    mensagem = f"O número {numero_informado} não pertence à sequência de Fibonacci."

print(mensagem)
