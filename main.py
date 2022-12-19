# Calculator

# A intenção é criar uma calculadora com dois cálculos, Primeiro, criou uma função para cada operação,
# passando dois parâmetros e o que a função deve fazer, depois criou um dicionário: operations,
# que transformou cada símbolo em uma chave e o nome da função no seu correspondente, depois pede
# o primeiro número pelo input, que ele já transforma em int, então criou um for loop para iterar
# pelo dicionário e imprimir cada símbolo, lembrando que o for loop só itera pelas chaves, define
# e pede o operation_symbol, pede o num 2, cria a calculation_function que é o símbolo escolhido
# por input, mas passado por [] para o correspondente no dicionário que é o correspondente nas funções,
# define então que first_answer é o calculation_function passado com os dois parâmetros que entram pelo input,
# imprime a operação toda (o cálculo não é feito no print, só imprime cada input correspondente),
# pede novamente o símbolo e dessa vez passa o first_answer como primeiro parâmetro (no vídeo o primeiro
# código dava um bug pois mantinha o primeiro símbolo escolhido)
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

# Here we select "+"
operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# Here we select "*" which overides the "+" we selected on line 26.
operation_symbol = input("Pick an operation: ")
num3 = int(input("What's the next number?: "))

# Here the calculation_function selected will be the multiply() function
calculation_function = operations[operation_symbol]

# Here the code will be:
# second_answer = multiply(multiply(num1, num2), num3)
second_answer = calculation_function(calculation_function(num1, num2), num3)
# second_answer = 2 * 3 * 3 = 18
# To fix this bug we need to change the code on line 42 to:
second_answer = calculation_function(first_answer, num3)
# In the next lesson, we will delete all the code from line 34-48 so don't worry
# It won't affect your final project.
# But it's a good oportunity to practice debugging. 🐞

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# O código foi atualizado para incluir um while loop que pergunta se deseja incluir um novo número após o segundo,
# então ele transforma o answer no primeiro número e continua, quando a resposta é n ou qualquer outra, ele chama
# a função clear()
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()

