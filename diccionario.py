#Creando un diccionario simple
cancion={
'artista' : 'Amaro',
'Cancion':'Amor de Antes',
'Lanzamiento': 2014,
'Likes' : 104.07,
}# esto es un diccionario 

#Aceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['Lanzamiento'])
print(cancion['Cancion'])
print(cancion['Likes'])



#Mezclar con un Str
print(f'Estoy escuchando a: {cancion["artista"]} con el tema, {cancion["Cancion"]}, que fue lanzada en el año {cancion["Lanzamiento"]} y tuvo {cancion["Likes"]} de Likes')
cancion['PlayList'] = 'Raggaeton'
print(cancion)

#Remplazar valores
cancion['cancion'] = 'Un sueño'
print(cancion)

#Eliminar un valor 
del cancion['Lanzamiento']
print(cancion)

cancion['Lanzamiento' : 2012]
print(cancion)