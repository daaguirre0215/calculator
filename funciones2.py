def informacion(nombre, puesto):
    print(f'Mi nombre es: {nombre} y soy {puesto}')

informacion('Daniel','Desarrollador')
informacion('Aaron','Diseñador')
informacion('Gabi','Secretaria')

def lenguaje(lenguajes_de_programacion, nivel_lenguaje = '(sin argumentos)'):
    print(f'Nombre del Lenguaje: {lenguajes_de_programacion} y es de {nivel_lenguaje}')

lenguaje('Java','Alto Nivel')
lenguaje('PHP','Alto Nivel')
lenguaje('Python','Alto Nivel')
lenguaje('C#','Alto Nivel\n')

lenguaje('Codigo Binario','Bajo Nivel')
lenguaje('Lenguaje de máquina','Bajo Nivel')
lenguaje('lenguajes Ensambladores','Bajo Nivel')