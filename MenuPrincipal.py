import os
os.system("cls")

import Trabajador
import CargaFamiliar
import ContactoEmergencia

def MenuPrincipal():
    repeat = True

    print("--Menu principal--")
    print("1 Trabajador")
    print("2 Carga Familiar")
    print("3 Contacto Emergencia")
    print("4 Salir")
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        Trabajador()

    if opcion == 2:
        CargaFamiliar()

    if opcion == 3:

        ContactoEmergencia()

    if opcion == 4:
        repeat = False
    


    return repeat

def ejecucion():
    while(MenuPrincipal()):
        pass


ejecucion()
