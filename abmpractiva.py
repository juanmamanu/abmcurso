#Simulador de ABM
#agregar regla de simbolos especiales para usuarios, passwords e is numeric edad

#importar

import json
import os

#Declaración de funciones
class Usuario:
    
    def __init__(self, usuario, nombre, edad, passsword):
        self.usuario = usuario
        self.nombre = nombre
        self.edad = edad
        self.password = passsword
    

    def __str__(self):
        return f"usuario:{self.usuario} , Nombre:{self.nombre}, Edad:{self.edad}"

    def validar_datos_usuarios(self):
        usuario_valido = True
        regla_string_usuario_valido = (not self.usuario[0].isnumeric() and len(self.usuario) > 4)
        regla_nombre_valido = len(self.nombre) > 3
        regla_edad_valido = (self.edad.isnumeric() and self.edad > 15)
        regla_password = len(self.password) > 4 and '#' in self.password or '%' in self.password

        if not regla_string_usuario_valido:
            print("Usuario: No puede empezar con un Número y Tienen que Ser mayor a 4 caracteres")
            usuario_valido = False

        if not regla_nombre_valido:
            print("Nombre: Tiene que ser mayor a 3 caracteres")
            
        if not regla_edad_valido:
            print("Edad tiene que ser un entero y mayor a 15")
            usuario_valido = False

        if not regla_password:
            print("El password tiene que ser mayor a 4 caracteres y tiene que tener un # o %")
            usuario_valido = False

        return usuario_valido



class MenuAbm:
    def __init__(self, usuarios=dict()):
        self.usuarios=usuarios


    def __crear_usuario(self):
        usuario_valido= True
        
        print("crear usuario\n")
        usuario = input("Usuario: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        password = input("Password: ")
        password_dos = input("Repita el password: ")

        nuevo_usuario = Usuario(usuario, nombre, edad, password)
        usuario_valido = nuevo_usuario.validar_datos_usuarios()

        regla_usaurio_repetido = (usuario in self.usuarios)
        regla_repetir_password = password == password_dos

        if not regla_repetir_password:
            print("Los passwords no coinciden.")
            usuario_valido = False
        if regla_usaurio_repetido:
            print("El usuario ingresado ya existe")
            usuario_valido = False

        if not usuario_valido:
            print("Corrija los errores")
        else:
            self.usuarios[usuario] = nuevo_usuario.__dict__

    def __buscar_usuario(self):
        criterio = input("Ingrese el Usuario que esta buscando: ")
        resultado = self.usuarios.get(criterio, f"No existe el Usuario {criterio}")
        print(resultado)

    def __borrar_usuario(self):
        criterio = input("Ingrese el Usuario que esta buscando: ")
        resultado = usuarios.get(criterio, False)
        if resultado:
            del self.usuarios[criterio]
        else:
            print("No existe ese Usuario")

    def __modificar_usuario(self):
        criterio = input("Ingrese el Usuario que desea modificar: ")
        usuario_encontrado = self.usuarios.get(criterio, False)
        
        if not usuario_encontrado:
            print("No existe ese Usuario")
        else:
            nombre = input("Nombre:")
            edad = input("Edad:")
            password = input("Password: ")
            password_dos = input("Repita el password:")
            
            usuario_valido = True
            usuario_modificado = Usuario(criterio, nombre, edad, password)
            usuario_valido = usuario_modificado.validar_datos_usuario()
            regla_repetir_password = password == password_dos

            if not regla_repetir_password:
                print("Los passwords no coinciden.")
                    
            if not usuario_valido:
                print("Corrija los errores")

            else:
                usuarios[criterio] = usuario_modificado.__dict__
                print(f"Se modificó con éxito {usuario_encontrado}")

    def mostrar_menu(self):
        print("Ingrese su opcion")
        print("1)-Crear nuevo usuario")
        print("2)-Borar un usuario")
        print("3)-Modificar un usuario")
        print("4)-Buscar un usuario")
        print("5)-Mostrar usuarios")
        print("6)-cerrar")


    def leer_operacion(self):
        operacion = input("Ingrese operacion: ")
        if operacion == "1":
            self.__crear_usuario()
        elif operacion == "2":
            self.__buscar_usuario()
        elif operacion == "3":
            self.__borrar_usuario()
        elif operacion == "4":
            self.__modificar_usuario()
        elif operacion == "5":
            print("Se sale del programa.")
            self.__persistir()
            return True    
        else:
            print("La operación ingresada no existe")
        
        self.__persistir()
        return False

    def __persistir(self):
        with open("usuarios.json", "w") as archivo:
            archivo.writelines(json.dumps(self.usuarios, indent=2))


# Inicio de mi script

if __name__ == "__main__":

    usuarios = dict()

    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:        
            usuarios = json.load(archivo)
    
    menu_abm_usuarios = MenuAbm(usuarios)
    
    while True:
        menu_abm_usuarios.mostrar_menu()
        salir = menu_abm_usuarios.leer_operacion()
        if salir:
            break








"""
segundo menu
if __name__ == "__main__":
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:        
            usuarios = json.load(archivo)
    else:
        usuarios = dict()
    while True:
        mostrar_menu()    
        operacion = input("Ingrese operacion: ")
        if operacion == "1":
            crear_usuario()
        elif operacion == "2":
            buscar_usuario()
        elif operacion == "3":
            borrar_usuario()
        elif operacion == "4":
            modificar_usuario()
        elif operacion == "5":
            mostrar_usuarios()
        elif operacion == "6":
            print("Se sale del programa.")
            persistir()
            break   
        
        else:
            print("La operación ingresada no existe")
        persistir() 
"""





"""

primer menu
while True:
    
    mostrar_menu()
    menu = input("Indique su opcion ")
    if menu == "1":
        crear_usuario()
    elif menu == "2":# Opcion N2 para borrar usuario
        borrar_usuario() 
    elif menu == "3": #Opcion N3 para modificar el usuariomenu = input("Indique su opcion\n 1)-Crear nuevo usuario\n 2)-Borar un usuario\n 3)-Modificar un usuario\n 4)-Buscar un usuario\n 5)-Mostrar lista de usuarios\n 6)-cerrar\n")     
        modificar_usuario()
    elif menu == "4":#Opcion N4 para buscar un usuario por llaves
        buscar_usuario()
    elif menu == "5":# lista de usuarios REVEEEER
        imprimir_usuarios()
    elif menu == "6": #cierra el bucle o retorna menu
        salir = input("1)-Si\n2)-No\n")
        if salir == "1":
            print("Cierre de ejecucion ")
            break
        else:
            mostrar_menu()
    else:
        print("¡¡¡¡¡¡¡ingrese una opcion valida!!!!")
        print("¡¡¡¡¡¡¡ingrese una opcion valida!!!!")
        mostrar_menu()
"""
