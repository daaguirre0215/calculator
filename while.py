pregunta = 'Agrega un número y te diré si es par o  no \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación...)\r\n'
preguntar = True

while preguntar:

    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 ==0:
            print(f'El numero: {numero} es par \r\n')
else:
    print(f'El número: {numero} es impar \r\n')