from ntpath import realpath
import os, sqlite3
os.system("cls")

conn = sqlite3.connect("TRABAJO.db")
miCursor = conn.cursor()

class ContactoEmergencia:
    def __init__(self, rut_ce, nombre, apellido, relacion, telefono):
        self.rut_ce = rut_ce
        self.nombre = nombre
        self.apellido = apellido
        self.relacion = relacion
        self.telefono = telefono
# AGREGAR
def AgregarContacto():
    rut_ce = input("Ingresar rut: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    relacion = input("Relacion con el trabajador")
    telefono = input("Telefono del contacto: ")

    a = ContactoEmergencia(rut_ce, nombre, apellido, relacion, telefono)
    
    miCursor.execute("SELECT * FROM CONTACTO_EMERGENCIA WHERE rut_ce = {}".format(a.rut_ce))
    Validacion = miCursor.fetchall()

    if len(Validacion) == 0:
        miCursor.execute("INSERT INTO CONTACTO_EMERGENCIA VALUES('{}', '{}', '{}', '{}', '{}')". format(a.rut_ce, a.nombre, a.apellido, a.relacion, a.telefono))
        conn.commit()
        print("Datos creados exitosamente")
    else:
        print("Error, Contacto ya existe")
# MODIFICAR
def ModificarContacto():
    rut_ce = input("Ingrese rut que desea modificar: ")
    miCursor.execute("SELECT * FROM CONTACTO_EMERGENCIA WHERE rut_ce = {}".format(rut_ce))

    listaContacto = miCursor.fetchall()

    if len(listaContacto) == 0:
        print("No se puede modificar contacto de emergencia")
    else:
        print("El nombre que desea editar es {} ¿Desea cambiarlo? 1.Si 2.No".format(listaContacto[0][1]))
        
        opcion = int(input())

        if opcion == 1:
            nombre = input("Ingrese nuevo nombre del familiar: ")
        else:
            if opcion==2:
                nombre = listaContacto[0][1]
        print("El apellido del familiar ahora es {} ¿Desea cambiarlo? 1.Si 2.No".format(listaContacto[0][2]))

        opcion = int(input())
        
        if opcion == 1:
            apellido = input("Ingrese el nuevo apellido del trabajador: ")
        else:
            if opcion==2:
                apellido = listaContacto[0][2]    

        print("Desea cambiar la relacion que es {} ¿Desea cambiarlo? 1. Si 2. No".format(listaContacto[0][3]))

        opcion = int(input())

        if opcion == 1:
            relacion = input("Ingrese relacion que tiene el contacto con el trabajador: ")
        else:
            if opcion==2:
                relacion = listaContacto[0][3]    

        print("El numero de telefono que es {}  ¿Desea cambiarlo? 1. Si 2. No".format(listaContacto[0][4]))

        opcion = int(input())

        if opcion == 1:
            telefono = input("Ingrese telefono del contacto: ")
        else:
            telefono = listaContacto[0][4]    

        miCursor.execute("UPDATE CONTACTO_EMERGENCIA SET nombre = '{}', apellido = '{}', relacion = '{}', telefono = '{}' WHERE rut_ce = {} ".format(nombre, apellido, relacion, telefono, rut_ce))    
        conn.commit()
        print("El codigo con rut {} se modifico".format(rut_ce))
# LISTAR
def ListarContacto():
    miCursor.execute("SELECT * FROM CONTACTO_EMERGENCIA")
    listaFamiliar = miCursor.fetchall()

    for contacto in listaFamiliar:
        print("rut_t: {}, nombre: {}, apellido: {}, relacion: '{}', telefono: '{}'".format(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4]))
# ELIMINAR
def EliminarContacto():
    rut_ce = input("Ingrese el rut que desea eliminar: ")
    miCursor.execute("SELECT * FROM CONTACTO_EMERGENCIA WHERE rut_ce = {}".format(rut_ce))

    listaTrabajador = miCursor.fetchall()

    if len(listaTrabajador) == 0:
        print("Error, no se puede eliminar la carga familiar, debido a que no existe")
    else:
        miCursor.execute("DELETE FROM CONTACTO_EMERGENCIA WHERE rut_ce = {}".format(rut_ce))
        conn.commit()
        print("Contacto eliminado correctamente")

def MenuContacto():
    repeat = True

    print("--Menu Contacto Emergencia--")
    print("1 Agregar")
    print("2 Modificar")
    print("3 Listar")
    print("4 Eliminar")
    print("5 Salir")
    print("------------------------------")
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        AgregarContacto()
    
    if opcion == 2:
        ModificarContacto()

    if opcion == 3:
        ListarContacto()

    if opcion == 4:
        EliminarContacto()
    
    if opcion == 5:
        repeat = False
    
    return repeat

def ejecucionContacto():
    while (MenuContacto()):
        pass

ejecucionContacto()