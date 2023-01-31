#Iniciar un diccionario vacio

jugador = {}
print(jugador)

# Se une un jugador 
jugador['Nombre'] = 'Aarón'
jugador['Puntaje'] = 0
print(jugador)

#Incrementando el puntaje 
jugador['Puntaje'] = 100
print(jugador)

#Incrementando el puntaje 
jugador['Puntaje'] = 200
print(jugador)

#Incrementando el puntaje 
jugador['Puntaje'] = 300
print(jugador)

#Incrementando el puntaje 
jugador['Puntaje'] = 400
print(jugador)

print(jugador.get('Consola'))
print(jugador.get('Puntaje'))

#Acceder a un valor 
print(jugador.get('Consola',' No existe ese valor'))

# Iterar en el diccionario
for llave,valor in jugador.items():
    print(llave)
    print(valor)

# Eliminar jugador y puntaje
del jugador['Nombre']
del jugador['Puntaje']
print(jugador)