# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.

soma = 0
# Loop para receber números e somá-los até que 0 seja digitado
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break 
    soma += numero
# Exibe o valor total
print(f"O valor total é: {soma}")