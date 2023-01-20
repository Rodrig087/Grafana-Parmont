# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:08:58 2022

@author: milto
"""

import sqlite3
import psycopg2

# Conexion a las bases de datos
conSQlite = sqlite3.connect("/home/milton/Escritorio/PlataformaIot/BaseDatos/Pruebas/home-assistant_v2.db")
conPostgres = psycopg2.connect("host=localhost dbname=admin user=admin password=.MUNpos2022.")

curSQLite = conSQlite.cursor()
curPostgres = conPostgres.cursor()

# Selecciona la entidad:
#1. sensor.temperatura_estudio
#2. sensor.humedad_estudio

res_SQLite  = curSQLite.execute("SELECT state_id, entity_id, state, last_changed, last_updated FROM states WHERE entity_id = 'sensor.humedad_estudio'")
numDatos = 1000

#-------------------------------------------------------------------------------------------------------------
# Agregar elementos a PostgreSQL:
banAgregar = 0
if (banAgregar==1):
    for i in range(numDatos):
        lista_SQLite = res_SQLite.fetchone();
        print(lista_SQLite)
        es_Postgres = curPostgres.execute("""INSERT INTO public.states(state_id, entity_id, state, last_changed, last_updated) VALUES (%s, %s, %s, %s, %s);""" , (lista_SQLite[0], lista_SQLite[1], lista_SQLite[2], lista_SQLite[3], lista_SQLite[4]))
        # Hacer que los cambios en la base de datos sean persistentes
        conPostgres.commit()
#-------------------------------------------------------------------------------------------------------------
# Borrar elementos de PostgreSQL:
banBorrar = 0
if (banBorrar==1):
    for i in range(numDatos):
        lista_SQLite = res_SQLite.fetchone();
        print(lista_SQLite[0])
        res_Postgres = curPostgres.execute("DELETE from public.states WHERE state_id = %s" , (lista_SQLite[0],))
        # Hacer que los cambios en la base de datos sean persistentes
        conPostgres.commit()
#-------------------------------------------------------------------------------------------------------------
# Listar elementos de PostgreSQL:
banListar = 0
if (banListar==1):
    print(' ')
    curPostgres.execute("SELECT * FROM public.states")
    for i in range(2000):
        lista_Postgres = curPostgres.fetchone()
        print(lista_Postgres)
#-------------------------------------------------------------------------------------------------------------
# Consultas:
banConsulta = 1
if (banConsulta==1):
    print(' ')
    curPostgres.execute("SELECT last_updated AS time, state AS metric FROM states WHERE state <> 'unavailable' AND state <> 'unknown' AND entity_id = 'sensor.humedad_estudio'")
    for i in range(1000):
        lista_Postgres = curPostgres.fetchone()
        print(lista_Postgres)
