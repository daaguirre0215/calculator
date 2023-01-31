lenguajes = ['Java','Python','JavaScript','Ruby','C++']
print(lenguajes)

lenguajes.sort()# Permite ordenar alfabéticamente una list
print(lenguajes)

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

lenguajes[2] = 'PHP'#Modificando un List (LISTA)
print(lenguajes)

# Agregar elemnto a un list
lenguajes.append('C#')
print(lenguajes)

#Eliminar elemento de una list
del lenguajes[0]
print(lenguajes)

#Eliminar el ultimo elemento de una list
lenguajes.pop()
print(lenguajes)

#Eliminar con POP un elemento especifico de una list
lenguajes.pop(3)
print(lenguajes)

#Eliminar elemento de una list por nombre 
lenguajes.remove('Java')
print(lenguajes)

lenguajes.append('Java')
print(lenguajes)

aprendiento2= f'Estoy aprendiendo {lenguajes[1]}'
print(aprendiento2)
