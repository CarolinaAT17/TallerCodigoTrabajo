import os
os.system("cls")

def ContactoEmergencia():
    repeat = True

    print("--Menu Contacto Emergencia--")
    print("1 Agregar")
    print("2 Modificar")
    print("3 Listar")
    print("4 Salir")
    opcion = int(input())

    if opcion == 1:
        AgregarContacto()
    
    if opcion == 2:
        ModificarContacto()

    if opcion == 3:
        ListarContacto()
    
    if opcion == 4:
        repeat = False
    
    return repeat