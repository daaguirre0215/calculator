'''nombre = input('¿Cúal es tu nombre? \r\n ' )
print(f'Hola {nombre}, un gusto')'''

# Leer datos que serán numeros
'''nota_1 = input('¿Cúal fue tu nota en el primer parcial?\r\n ')

# Convertir Str 'Edad 'a entero (int)
nota_1 = float(nota_1) # Convertimos edad a int

if nota_1 <=5.9:
    print('Reprobaste, iras a complementario')
else:
    print('Felicidades, pasaste la materia')'''

#Mezclarlo con operadores 
numero = input('Agrega un número y te diré si es par o  no \r\n')

# convertimos a int
numero = int(numero)
if numero % 2==0:
    print(f'El numero: {numero} es par')
else:
    print(f'El número: {numero} es impar')