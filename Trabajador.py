import os
os.system("cls")

def Trabajador():
    repeat = True

    print("--Menu trabajadores--")
    print("1 Agregar")
    print("2 Modificar")
    print("3 Listar")
    print("4 Salir")
    opcion = int(input())

    if opcion == 1:
        AgregarTrabajador()
    
    if opcion == 2:
        ModificarModificar()

    if opcion == 3:
        ListarModificar()
    
    if opcion == 4:
        repeat = False
    
    return repeat

def ejecucionTrabajador():
    while (Trabajador()):
        pass
ejecucionTrabajador()