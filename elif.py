# Ejemplo con Elif 
ocupacion = 'Nada'

if ocupacion == 'Estudiante':
    print('Tienes 50% de Descuento')

elif ocupacion == 'Jubilado':
    print('Tienes el 75% de Descuento')
elif ocupacion == 'Desempleado':
    print('Tienes el 10% de Descuento')
else:
    print('Debes pagar el 100%')