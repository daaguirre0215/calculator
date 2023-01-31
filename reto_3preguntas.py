#Puntuación
puntuacion_1 = 3.33
puntuacion_2 = 3.33
puntuacion_3 = 3.34

#Preguntas 
pregunta_1 = '¿Python es un lenguaje de programación de alto nivel?'
pregunta_2 = '¿Java es un lenguaje de programación orientado a objetos?'
pregunta_3 = '¿Java y JavaScript son lo mismo?'

#Respuestas
respuesta_1 = 'si'
respuesta_2 = 'si'
respuesta_3 = 'no'

#sumatoria de puntuación
suma_total = puntuacion_1+puntuacion_2+puntuacion_3

print('------------------------')
print('EXAMEN DE TRES PREGUNTAS')
print('------------------------')
print('Conteste, si o no \r\n')

pregunta_uno = input(f'1-{pregunta_1}\r\n¡Conteste, si o no!: ')
if pregunta_uno == respuesta_1:
    print('Es correcto!!')
if pregunta_uno == respuesta_1:
    print(f'Tienes una puntuación de {puntuacion_1}\r\n')
else:
    print('Falso, la respuesta era "Si"')


pregunta_dos = input(f'2-{pregunta_2}\r\n¡Conteste, si o no!: ')
if pregunta_dos ==respuesta_2:
    print('Es correcto!!')
if pregunta_dos == respuesta_2:
    print(f'Tienes una puntuación de {puntuacion_2}\r\n')
else:
    print('Falso, la respuesta era "Si"')


pregunta_tres = input(f'{pregunta_3}\r\n¡Conteste, si o no!: ')
if pregunta_tres == respuesta_3:
    print('Es correcto, la respuesta es "No"')
if pregunta_tres == respuesta_3:
    print(f'Tienes una puntuación de {puntuacion_3}\r\n')
else:
    print('Falso, la respuesta era "No"\r\n')

print(f'Felicidades tienes una puntuación de {suma_total}')
