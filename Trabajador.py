import os
os.system("cls")


class Trabajador:
    def __init__(self, rut_f, nombre, apellido, direccion, telefono, fecha_ingreso):
        self.rut_f = rut_f
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

    miCursor.execute("SELECT * FROM TRABAJADOR WHERE rut_t")


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