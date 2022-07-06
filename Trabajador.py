import os, sqlite3
os.system("cls")

conn = sqlite3.connect("TRABAJO.db")
miCursor = conn.cursor()

class Trabajador:
    def __init__(self, rut_t, nombre, apellido, direccion, telefono, fecha_ingreso):
        self.rut_t = rut_t
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso

# AGREGAR
def AgregarTrabajador():
    rut_t = input("Ingresar rut: ")
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    direccion = input("Ingresar direccion: ")
    telefono = input("Ingresar telefono: ")
    fecha_ingreso = input("Ingresar fecha(dd-mm-yyyy): ")

    a = Trabajador(rut_t, nombre, apellido, direccion, telefono, fecha_ingreso)

    miCursor.execute("SELECT * FROM TRABAJADOR WHERE rut_t = {}".format(a.rut_t))
    Validacion = miCursor.fetchall()

    if len(Validacion) == 0:
          # Generar insert
        miCursor.execute("INSERT INTO CREDITO VALUES({}, '{}', {}, {}, {}, {})".format(a.rut_t, a.nombre, a.apellido, a.direccion, a.telefono. a.fecha_ingreso))
            # Guardar cambios
        conn.commit()
        print("Datos creados exitosamente")
    else:
        print("Error, no se puede agregar ya que la ID existe")
# Modificar
def ModificarTrabajador():
    rut_t = input("Ingrese el rut de trabajador a editar: ")
    miCursor.execute("SELECT * FROM PRODUCTO WHERE rut_t  = {}".format(rut_t))

    listaTrabajador= miCursor.fetchall()

    if len(listaTrabajador) == 0:
        print("Error, no se puede editar trabajador")
    else:
        print("El valor del nombre es {} ¿Desea cambiarlo? 1. Si 2. No".format(listaTrabajador[0][1]))
        
        op = int(input())

        if op == 1:
            nombre = input("Ingrese el nuevo nombre de trabajador: ")
        else:
            nombre = listaTrabajador[0][1]
        print("El nombre del trabajador es {} ¿Desea cambiarlo? 1. Si 2.No".format(listaTrabajador[0][2]))

        op = int(input())

        if op == 1:
            apellido = input("Ingrese el nuevo apellido del trabajador: ")
        else:
            apellido = listaTrabajador[0][2]    

        print("El apellido del trabajador es {} ¿Desea cambiarlo? 1. Si 2. No".format(listaTrabajador[0][3]))

        op = int(input())

        if op == 1:
            direccion = input("Ingrese la nueva direccion del trabajador: ")
        else:
            direccion = listaTrabajador[0][3]

        print("La direccion del trabajador es {} ¿Desea cambiarlo? 1. Si 2. No".format(listaTrabajador[0][4]))

        if op == 1:
            telefono = input("Ingrese la nueva direccion del trabajador: ")
        else:
            telefono = listaTrabajador[0][4]

        print("El telefono del trabajador es {} ¿Desea cambiarlo? 1. Si 2. No".format(listaTrabajador[0][5])) 

        miCursor.execute("UPDATE TRABAJADOR SET nombre = '{}', apellido = '{}', direccion = '{}', telefono = '{}' WHERE rut_t = {}".format(nombre, apellido, direccion, telefono, rut_t))    
        conn.commit()
        print("El Producto con ID: {} se actualizó correctamente".format(rut_t))
# Listar
def ListarTrabajador():
    miCursor.execute("SELECT * FROM TRABAJADOR")
    listaTrabajador = miCursor.fetchall()

    for trabajador in listaTrabajador:
        print("rut_t: {}, nombre: {}, apellido: {}, direccion: {}, telefono: {}, fecha_ingreso: {}".format(trabajador[0], trabajador[1], trabajador[2], trabajador[3], trabajador[4], trabajador[5]))


def MenuTrabajador():
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
        ModificarTrabajador()

    if opcion == 3:
        ListarTrabajador()
    
    if opcion == 4:
        repeat = False
    
    return repeat

def ejecucionTrabajador():
    while (MenuTrabajador()):
        pass
ejecucionTrabajador()