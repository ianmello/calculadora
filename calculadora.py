def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


print("Escolha uma operação.")
print("1.Soma")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")


while True:
    operação = input("Escolha uma operação(1/2/3/4): ")

    if operação in ('1', '2', '3', '4'):
        if operação == '1':
            print("Adição")
        elif operação == '2':
            print("Subtração")   
        elif operação == '3':
            print("Multiplicação") 
        elif operação == '4':
            print("Divisão")        

        try:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
        except ValueError:
            print("Número invalido. Insira apenas números.")
            continue

        if operação == '1':
            print(num1, "+", num2, "=", soma(num1, num2))

        elif operação == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif operação == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif operação == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))
        
        break
    else:
        print("Erro")