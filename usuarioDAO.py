from cursor_del_pool import CursorDelPool
from usuario import Usuario


class UsuarioDAO:
    _SQL = None
    _operacionExitosa = False

    @classmethod
    def select(cls):
        cls._SQL = 'SELECT * FROM usuario ORDER BY id_usuario'
        with CursorDelPool() as cursor:
            cursor.execute(cls._SQL)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
                # print(f'Existen {cursor.rowcount} usuarios registrados')
            return usuarios

    @classmethod
    def insert(cls, usuario):
        cls._SQL = 'INSERT INTO usuario (username, password) VALUES (%s, %s)'
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._SQL, valores)
            print(f'El usuario se insertó correctamente')

    @classmethod
    def update(cls, usuario):
        cls._SQL = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._SQL, valores)
            print(f'El usuario se actualizó correctamente')

    @classmethod
    def delete(cls, usuario):
        cls._SQL = 'DELETE FROM usuario WHERE id_usuario = %s'
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._SQL, valores)
            print(f'El usuario se eliminó correctamente')


if __name__ == '__main__':
    # Insertar un usuario
    # username = input('Ingrese el nombre de usuario: ')
    # password = input('Ingrese la contraseña del usuario: ')
    # usuario1 = Usuario(username=username, password=password)
    # UsuarioDAO.insert(usuario1)

    # Actualizar un usuario
    # id_usuario = input('Ingrese el id del usuario: ')
    # username = input('Ingrese el nombre de usuario: ')
    # password = input('Ingrese la contraseña del usuario: ')
    # usuario1 = Usuario(id_usuario, username, password)
    # UsuarioDAO.update(usuario1)

    # Eliminar usuario
    # id_usuario = input('Ingrese el id del usuario: ')
    # usuario1 = Usuario(id_usuario=id_usuario)
    # UsuarioDAO.delete(usuario1)

    usuarios = UsuarioDAO.select()
    for usuario in usuarios:
        print(usuario)
