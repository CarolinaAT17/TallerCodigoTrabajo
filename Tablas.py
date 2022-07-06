import os, sqlite3
os.system("cls")
import sqlite3
conn = sqlite3.connect("TRABAJO.db")
miCursor = conn.cursor()

# CREACION DE TABLAR Y PRIMARY KEY
miCursor.execute("CREATE TABLE IF NOT EXISTS COMUNA(cod_comuna NUMBER PRIMARY KEY, nombre VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS TRABAJADOR(rut_t NUMBER PRIMARY KEY NOT NULL, nombre VARCHAR2(50), apellido VARCHAR2(50), direccion VARCHAR2(50), telefono VARCHAR2(12), fecha_ingreso VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS CARGO(cod_cargo NUMBER PRIMARY KEY, nombre_cargo VARCHAR2(20));")
miCursor.execute("CREATE TABLE IF NOT EXISTS DEPARTAMENTO(cod_departamento NUMBER PRIMARY KEY, nombre VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS GENERO(cod_genero NUMBER PRIMARY KEY, nombre VARCHAR2(20));")
miCursor.execute("CREATE TABLE IF NOT EXISTS CARGA_FAMILIAR(rut_cf NUMBER PRIMARY KEY NOT NULL, nombre VARCHAR2(50), apellido VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS PARENTEZCO(cod_parentezco NUMBER PRIMARY KEY,nombre VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS CONTACTO_EMERGENCIA(rut_ce NUMBER PRIMARY KEY NOT NULL, nombre VARCHAR2(50), apellido VARCHAR2(50), relacion VARCHAR2(20), telefono VARCHAR2(12));")

# ASIGNACION DE FOREIGN KEY

miCursor.execute("CREATE TABLE IF NOT EXISTS COMUNA(cod_comuna NUMBER PRIMARY KEY, nombre VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS TRABAJADOR(rut_t NUMBER PRIMARY KEY NOT NULL, nombre VARCHAR2(50), apellido VARCHAR2(50), direccion VARCHAR2(50), telefono VARCHAR2(12), fecha_ingreso VARCHAR2(50), FOREIGN KEY(cod_comuna) REFERENCES COMUNA(cod_comuna), FOREIGN KEY(cod_cargo) REFERENCES CARGO(cod_cargo), FOREIGN KEY(cod_genero) REFERENCES GENERO(cod_genero), FOREIGN KEY(cod_departamento) REFERENCES DEPARTAMENTO(cod_departamento), FOREIGN KEY(rut_cf) REFERENCES CARGA_FAMILIAR(rut_cf), FOREIGN KEY(rut_ce) REFERENCES CONTACTO_EMERGENCIA(rut_ce));")
miCursor.execute("CREATE TABLE IF NOT EXISTS CARGO(cod_cargo NUMBER PRIMARY KEY, nombre_cargo VARCHAR2(20));")
miCursor.execute("CREATE TABLE IF NOT EXISTS DEPARTAMENTO(cod_departamento NUMBER PRIMARY KEY, nombre VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS GENERO(cod_genero NUMBER PRIMARY KEY, nombre VARCHAR2(20));")
miCursor.execute("CREATE TABLE IF NOT EXISTS CARGA_FAMILIAR(rut_cf NUMBER PRIMARY KEY NOT NULL, nombre VARCHAR2(50), apellido VARCHAR2(50), FOREIGN KEY (cod_parentezco) REFERENCES PARENTEZCO(cod_parentezco), FOREIGN KEY (rut_t) REFERENCES TRABAJADOR(rut_t), FOREIGN KEY (cod_genero_genero) REFERENCES GENERO(cod_genero));")
miCursor.execute("CREATE TABLE IF NOT EXISTS PARENTEZCO(cod_parentezco NUMBER PRIMARY KEY,nombre VARCHAR2(50));")
miCursor.execute("CREATE TABLE IF NOT EXISTS CONTACTO_EMERGENCIA(rut_ce NUMBER PRIMARY KEY NOT NULL, nombre VARCHAR2(50), apellido VARCHAR2(50), relacion VARCHAR2(20), telefono VARCHAR2(12), FOREIGN KEY (rut_t) REFERENCES TRABAJADOR(rut_t), FOREIGN KEY (cod_genero_genero) REFERENCES GENERO(cod_genero));")