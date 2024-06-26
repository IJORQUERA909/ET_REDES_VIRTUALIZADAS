usuarios = {} # Se genera el diccionario usuarios

def Registrar():
    global usuarios
    nombre = input("Ingrese nombre y apellido: ")
    rut = int(input("Ingrese RUT (Sin puntos ni guión): "))
    print("---------------------------------")
    print("---------------------------------")
    print("Usuario registrado de forma exitosa")
    print("---------------------------------")
    print("---------------------------------")

    usuarios[rut] = nombre, rut

    # Se hace referencia al diccionario, dejando en corchetes la clave que se usará
    # Se indica que valores serán considerados en la clave


def Buscar(): # Funcion para búsqueda de usuario con ciclo while que repetirá la opción si no se ingresa el dato correcto
    global usuarios
    x = 0
    while x == 0:
        b = int(input("Ingresar RUT de usuario, sin puntos ni guión (para volver al menú principal ingrese '0'): "))
        print("---------------------------------")
        if b in usuarios:
            print("Usuario: ", usuarios.get(b))
        elif b == 0:
            menu()
        else:
            print("Usuario no encontrado, vuelve a intentar :( ")

def listar():
    global usuarios
    print(usuarios)


def menu():
    i = 0
    while i == 0:
        print("---------------------------------")
        print("---------------------------------")
        print("REGISTRO Y CONSULTA DE USUARIOS")
        print("---------------------------------")
        print("---------------------------------")
        print("1. Registrar Usuario")
        print("2. Consultar Usuario")
        print("3. Listar usuarios")
        print("4. Salir")
        print("---------------------------------")
        print("---------------------------------")
        opcion = int(input("Ingresar opción: "))
        print("---------------------------------")
        print("---------------------------------")

        if opcion==1:
            print("-----REGISTRAR NUEVO USUARIO-----")
            print("---------------------------------")
            Registrar()
        elif opcion==2:
            print("-------CONSULTA DE USUARIOS------")
            print("---------------------------------")
            Buscar()
        elif opcion==3:
            listar()
        elif opcion==4:
            print("Gracias por su prferencia :)")
            exit()
        else:
            print("Opcion inválida, ingresar valor correcto :( ")
menu()








