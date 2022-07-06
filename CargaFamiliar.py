import os, sqlite3
os.system("cls")

conn = sqlite3.connect("TRABAJO.db")
miCursor = conn.cursor()

class CargaFamiliar:
    def __init__(self, rut_cf, nombre, apellido):
        self.rut_cf = rut_cf
        self.nombre = nombre
        self.apellido = apellido

# AGREGAR
def AgregarFamiliar():
    rut_cf = input("Ingresar rut: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")

    a = CargaFamiliar(rut_cf, nombre, apellido)
    
    miCursor.execute("SELECT * FROM CARGA_FAMILIAR WHERE rut_cf = {}".format(a.rut_cf))
    Validacion = miCursor.fetchall()

    if len(Validacion) == 0:
        miCursor.execute("INSERT INTO CARGA_FAMILIAR VALUES({}, '{}', '{}')". format(a.rut_cf, a.nombre, a.apellido))
        conn.commit()
        print("Datos creados exitosamente")
    else:
        print("Error, Familiar ya existe")
# MODIFICAR
def ModificarFamiliar():
    rut_cf = input("Ingrese rut que desea modificar: ")
    miCursor.execute("SELECT * FROM CARGA_FAMILIAR WHERE rut_cf = {}".format(rut_cf))

    listaFamiliar = miCursor.fetchall()

    if len(listaFamiliar) == 0:
        print("No se puede modificar carga familiar")
    else:
        print("El rut del familiar que desea editar es {} ¿Desea cambiarlo? 1.Si 2.No".format(listaFamiliar[0][1]))
        
        opcion = int(input())

        if opcion == 1:
            nombre = input("Ingrese nuevo nombre del familiar: ")
        else:
            nombre = listaFamiliar[0][1]
        print("El nombre del familiar ahora es {} ¿Desea cambiarlo? 1.Si 2.No".format(listaFamiliar[0][2]))

        opcion = int(input())
        
        if opcion == 1:
            apellido = input("Ingrese el nuevo apellido del trabajador: ")
        else:
            apellido = listaFamiliar[0][2]    

        print("El apellido del trabajador es {} ¿Desea cambiarlo? 1. Si 2. No".format(listaFamiliar[0][3]))

        op = int(input())

        miCursor.execute("UPDATE TRABAJADOR SET nombre = '{}', apellido = '{}' ".format(nombre, apellido))    
        conn.commit()
        print("La carga familiar con rut {} se modifico".format(rut_cf))
# LISTAR
def ListarFamiliar():
    miCursor.execute("SELECT * FROM CARGA_FAMILIAR")
    listaFamiliar = miCursor.fetchall()

    for familiar in listaFamiliar:
        print("rut_t: {}, nombre: {}, apellido: {}".format(familiar[0], familiar[1], familiar[2]))

def MenuFamiliar():
    repeat = True

    print("--Menu Carga Familiar--")
    print("1 Agregar")
    print("2 Modificar")
    print("3 Listar")
    print("4 Salir")
    print("------------------------------")
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        AgregarFamiliar()
    
    if opcion == 2:
        ModificarFamiliar()

    if opcion == 3:
        ListarFamiliar()
    
    if opcion == 4:
        repeat = False
    
    return repeat


def ejecucionFamiliar():
    while(MenuFamiliar()):
        pass    

ejecucionFamiliar()