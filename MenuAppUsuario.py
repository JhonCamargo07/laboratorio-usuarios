from usuario import Usuario
from usuarioDAO import UsuarioDAO


def opcionesUsuario():
    print('Opciones:\n1. Listar usuarios\n2. Agregar usuario\n3. Modificar usuario\n4.Eliminar usuario\n5. Salir')
    opcion = input('Eligue una opción: ')
    return opcion


def datosUsuario(accion):
    if accion == 'insert':
        username = input('Ingrese el nombre de usuario: ')
        password = input('Ingrese la contraseña del usuario: ')
        usuario = Usuario(username=username, password=password)
        return usuario
    elif accion == 'update':
        id_usuario = input('Ingrese el id del usuario: ')
        username = input('Ingrese el nombre de usuario: ')
        password = input('Ingrese la contraseña del usuario: ')
        usuario = Usuario(id_usuario, username, password)
        return usuario
    elif accion == 'delete':
        id_usuario = input('Ingrese el id del usuario: ')
        usuario = Usuario(id_usuario)
        return usuario


try:
    print('Control de usuarios'.center(70, '='))
    opcion = opcionesUsuario()
    while opcion != '5':
        if opcion == '1':
            print('\nUsuarios registrados en la base de datos:')
            usuarios = UsuarioDAO.select()
            for usuario in usuarios:
                print(usuario)
            print()
        elif opcion == '2':
            print()
            usuario = datosUsuario('insert')
            UsuarioDAO.insert(usuario)
            print()
        elif opcion == '3':
            print()
            usuario = datosUsuario('update')
            UsuarioDAO.update(usuario)
            print()
        elif opcion == '4':
            print()
            usuario = datosUsuario('delete')
            UsuarioDAO.delete(usuario)
            print()
        opcion = opcionesUsuario()
    else:
        print()
        print('Gracias por utilizar nuestro sitio'.center(70, '='))
except Exception as e:
    print(f'Ocurrió una excepción: {e}')
