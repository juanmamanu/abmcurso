#Simulador de ABM

#importar

import json
import os

#Declaración de funciones
usuarios = dict()

def mostrar_menu():
    print(" ")
    print("1)-Crear nuevo usuario")
    print("2)-Borar un usuario")
    print("3)-Modificar un usuario")
    print("4)-Buscar un usuario")
    print("5)-Mostrar usuarios")
    print("6)-cerrar")
    
def crear_usuario():
    print("crear usuario\n")
    usuario = input("Usuario: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    password = input("Password: ")
    password_dos = input("Repita el password: ")
    
    regla_string_usuario_valido = (not usuario[0].isnumeric() and len(usuario) > 6)
    
    regla_usaurio_no_repetido = (usuario not in usuarios)
    
    regla_nombre_valido = len(nombre) > 3
    
    regla_edad_valido = edad.isnumeric()

    regla_password = len(password) > 3 and '#' in password or '%' in password

    regla_repetir_password = password == password_dos

    usuario_valido = True

    if not regla_string_usuario_valido:
        print("Usuario: No puede empezar con un Número y Tienen que Ser mayor a 6")
        usuario_valido = False

    if not regla_usaurio_no_repetido:
        print("Usuario ya existe")
        usuario_valido = False
        
    if not regla_edad_valido:
        print("Edad tiene que ser un entero")
        usuario_valido = False

    if not regla_password:
        print("EL password tiene que ser mayor a 3 caracteres y tiene que tener un # o %")
        usuario_valido = False    
    if not usuario_valido:
        print("Corrija los errores")
    else:
        usuarios[usuario] = (nombre, edad, password)

def borrar_usuario():
    print("Borrar usuario\n")
    criterio = input("Ingrese el Usuario desea borrar: ")
    resultado = usuarios.get(criterio, False)
    if resultado:
        del usuarios[criterio]
    else:
        print("No existe ese Usuario que desea borrar\n")
        
def modificar_usuario():
    print("modificar usuario")
    criterio = input("Ingrese el Usuario que desea modificar: ")
    resultado = usuarios.get(criterio, False)   
    if not resultado:
        print("No existe ese Usuario")
    else:
        nombre = input("Nombre:")
        edad = input("Edad:")
        password = input("Password: ")
        password_dos = input("Repita el password:")    
        usuario_valido = True
        regla_nombre_valido = len(nombre) > 3
        regla_edad_valido = edad.isnumeric()
        regla_password = len(password) > 3 and '#' in password or '%' in password
        regla_repetir_password = password == password_dos      
        if not regla_edad_valido:
            print("Edad tiene que ser un entero")
            usuario_valido = False
        if not regla_password:
            print("EL password tiene que ser mayor a 3 caracteres y tiene que tener un # o %")
            usuario_valido = False        
        if not usuario_valido:
            print("Corrija los errores")
        else:
            usuarios[criterio] = (nombre, edad, password)
            print(f"Usuario se modificó con éxito el usuario {criterio}")
            print((nombre, edad, password))
            
def buscar_usuario():
    print("Buscar usuario")
    busqueda = input("ingrese el usuario que desea buscar : ")
    resultado = usuarios.get(busqueda,"no existe el usuario")
    print(resultado)
    
def imprimir_usuarios():
    print("lista de usuarios usuarios")
    print(usuarios)
def mostrar_usuarios():
    print (f"{usuarios}")

def persistir():
    with open("usuarios.json", "w") as archivo:
        archivo.writelines(json.dumps(usuarios, indent=2))
# Inicio de mi script

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
