num1 = input('Insira o primeiro número: ')
num2 = input('Insira o segundo número: ')

def calculo():
    soma = int(num1) + int(num2)

    def guardar(valor, num1, num2, verificador):
        with open('valor.csv', 'a') as file:
            file.write(str(num1) + ' + ' + str(num2) + ' = ' + str(valor) + ' (' + str(verificador) + ')' '\n')
    

    if (soma % 2 == 0):
        print('É par')
        verificador = 'Par'
        guardar(soma, num1, num2, verificador)
    else:
        print('É impar')
        verificador = 'Impar'
        guardar(soma, num1, num2, verificador)


if(num1.isdigit() and num2.isdigit()):
    calculo()

else:
    while (True):
        print("\nInsira um número\n")

        num1 = input('Insira o primeiro número: ')
        num2 = input('Insira o segundo número: ')

        if (num1.isdigit() and num2.isdigit()):
            break
    
    calculo()