import os
os.system("cls")

def CargaFamiliar():
    repeat = True

    print("--Menu Carga Familiar--")
    print("1 Agregar")
    print("2 Modificar")
    print("3 Listar")
    print("4 Salir")
    opcion = int(input())

    if opcion == 1:
        AgregarFamiliar()
    
    if opcion == 2:
        ModificarFamiliar()

    if opcion == 3:
        ListarFamiliar()
    
    if opcion == 4:
        repeat = False
    
    return repeat


def ejecucion2():
    while(CargaFamiliar()):
        pass    

ejecucion2()