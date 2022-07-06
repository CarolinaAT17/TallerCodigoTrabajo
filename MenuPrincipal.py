import os,sqlite3
os.system("cls")

import Trabajador
import CargaFamiliar
import ContactoEmergencia

conn = sqlite3.connect("TRABAJO.db")
miCursor = conn.cursor()

def MenuPrincipal():
    repeat = True

    print("--Menu principal--")
    print("1 Trabajador")
    print("2 Carga Familiar")
    print("3 Contacto Emergencia")
    print("4 Salir")
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        Trabajador(Trabajador.MenuTrabajador)

    if opcion == 2:
        CargaFamiliar(CargaFamiliar.MenuFamiliar)

    if opcion == 3:
        ContactoEmergencia(ContactoEmergencia.MenuContacto)

    if opcion == 4:
        repeat = False
    
    return repeat

def ejecucion():
    while(MenuPrincipal()):
        pass


ejecucion()