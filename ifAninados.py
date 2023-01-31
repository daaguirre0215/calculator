lenguajes = ['Java', 'Python', 'JavaScript', 'Ruby', 'C++', 'PHP']
if 'PHP' in lenguajes:
    print('PHP, si existe')
else:
    print('No existe')

# IF aninados
usuario_autenticado =False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('Acceso total con (ADMIN)')
    else:
        print('Acceso al sistema')

else:
    print('Debes iniciar seccion')
