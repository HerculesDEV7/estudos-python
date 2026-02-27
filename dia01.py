# Minhas primeiras variáveis
"""nome = "Hercules"
idade = 28
altura = 1.73
estudando_python = True

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}m")
print(f"Estudando Python: {estudando_python}")
print(f"Olá, {nome}! Você tem {idade} anos e está indo muito bem!")

# Entrada de dados
nome = input("Qual é seu nome? ")
idade = input("Qual é sua idade? ")

print(f"Olá, {nome}! Você tem {idade} anos.")
print(f"Em 10 anos você terá {int(idade) + 10} anos.")"""

# Exercicios

"""🟢 Nível Fácil
Exercícios diretos usando o que você aprendeu hoje. Se ainda estiver inseguro com algum conceito, volte e releia antes de tentar."""
 
""" Exercício 1  [FÁCIL]
Apresentação pessoal
Crie variáveis com seu nome, idade, cidade e profissão desejada. Use uma f-string para exibir uma apresentação completa em uma única linha."""

"""nome = "Hercules"
idade = 28
cidade = "Jundiai"
profissão_desejada = "Desenvolvedor RPA"

print(f"Olá! Meu nome é {nome}, tenho {idade} anos, moro em {cidade} e quero ser {profissão_desejada}.")"""

"""Exercício 2  [FÁCIL]
Tipos de dados na prática
Crie uma variável de cada tipo (str, int, float, bool) e use a função type() para imprimir o tipo de cada uma."""

"""nome2 = "H"
idade2 = 28
altura2 = 1.73
esta_cansado = True

print(type(nome2))
print(type(idade2))
print(type(altura2))
print(type(esta_cansado))"""

"""Exercício 3  [FÁCIL]
Calculadora simples com input
Peça dois números ao usuário e exiba a soma, subtração, multiplicação e divisão entre eles."""

"""num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)"""

"""Exercício 4  [FÁCIL]
Troca de variáveis
Crie duas variáveis 'a = 10' e 'b = 20'. Troque os valores entre elas sem usar uma terceira variável e imprima o resultado antes e depois da troca."""

a = 10
b = 20

print(f"Antes: {a}, {b}")

a, b = b, a

print(f"Depois: {a}, {b}\n")
