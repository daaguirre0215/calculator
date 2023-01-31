# revisar si una condicional es mayor a 
from colorama import init, Fore
init()

balance = 500
if balance < 50:
    print(Fore.GREEN + 'Puedes pagar!!!!!!')
else:
    print(Fore.RED +'No puedes pagar, saldo insuficiente')

likes = 200
if likes >= 200:
    print(Fore.CYAN + 'Excelente, 200 likes')
else:
    print(Fore.BLUE +'Casi llegas')
    
# IF con texto
lenguaje = 'Python'
if lenguaje == 'Python':
    print('Excelente desicion')

#Evaluar un booleano
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else: 
    print('Debes iniciar seccion')
