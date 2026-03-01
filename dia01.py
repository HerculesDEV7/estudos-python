#Exercicios

"""Exercício 5  [MÉDIO]
Conversor de temperatura
Peça uma temperatura em Celsius ao usuário e converta para Fahrenheit e Kelvin. Exiba os três valores formatados com 2 casas decimais."""

"""temperatura = int(input("Digite a temperatura em grau celsius: "))

print(f"Temperatura em Celsius: {temperatura}")

fahrenheit = (temperatura * 9/5) + 32

print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}")

kelvin = temperatura + 273.15

print(f"Temperatura em kelvin: {kelvin:.2f}")"""

"""Exercício 6  [MÉDIO]
Ficha de cadastro formatada
Peça ao usuário: nome completo, idade, altura e salário. Exiba uma ficha formatada com todos os dados, altura com 2 casas decimais e salário com 2 casas decimais e símbolo R$."""

"""nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = float(input("Digite sua altura: "))
salario = float(input("Digite seu salário: "))


print("===== FICHA CADASTRAL =====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}")
print(f"Salário: R${salario:.2f}\n")
print("===========================")"""

"""Exercício 7  [MÉDIO]
Calculadora de IMC
Peça peso (kg) e altura (m) ao usuário. Calcule o IMC (peso dividido por altura ao quadrado) e exiba o valor com 2 casas decimais. Calcule também o peso ideal para a altura (usando IMC ideal = 22) e exiba.
💡 Dicas:
• IMC = peso / (altura * altura) ou peso / altura**2"""


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

print(f"Seu IMC é de: {imc:.2f}")

peso_ideal = 22*(altura**2)

print(f"Seu peso ideal é de: {peso_ideal:.2f}\n")