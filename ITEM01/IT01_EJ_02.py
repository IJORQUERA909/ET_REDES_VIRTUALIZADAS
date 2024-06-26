
def menu():
    i = 0
    while i == 0:
        global vlan7
        print("-------------------------")
        print("¿VLAN EXTENDIDA O NORMAL?")
        vlan=int(input("Ingresa la Vlan a consultar: "))


        if vlan in range (1, 1006):
            print("La VLAN ", vlan, " está dentro del rango normal")

        if vlan in range (1002,1006):
            print("Los ID de 1002 a 1005 se reservan para las VLAN Token Ring y FDDI")

        elif vlan == 0:
            print("La VLAN ", vlan, " no es valida")

        elif vlan in range (1006, 4095):
            print("La VLAN ", vlan, " está dentro del rango Extendido")

        elif vlan >= 4095:
            print("VLAN fuera de rango")

menu()


