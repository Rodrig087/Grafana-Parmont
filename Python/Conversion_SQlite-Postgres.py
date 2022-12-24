# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:08:58 2022

@author: milto
"""

import sqlite3
import psycopg2

# Conexion a las bases de datos
conSQlite = sqlite3.connect("/home/milton/Escritorio/PlataformaIot/BaseDatos/Pruebas/home-assistant_v2.db")
conPostgres = psycopg2.connect("dbname=milton user=milton")

curSQLite = conSQlite.cursor()
curPostgres = conPostgres.cursor()

res_SQLite  = curSQLite.execute("SELECT state_id, entity_id, state, last_changed, last_updated FROM states WHERE entity_id = 'sensor.temperatura_estudio'")
lista_SQLite = res_SQLite.fetchone();
print(lista_SQLite)
#print(lista_SQLite[1])

#res_Postgres = curPostgres.execute("INSERT INTO public.states(state_id, entity_id, state, last_changed, last_updated) VALUES (90078, 'sensor.temperatura_estudio', 'unavailable', NULL, '2022-12-10 19:03:56.006937')")
res_Postgres = curPostgres.execute("""INSERT INTO public.states(state_id, entity_id, state, last_changed, last_updated) VALUES (%s, %s, %s, %s, %s);""" , (lista_SQLite[0], lista_SQLite[1], lista_SQLite[2], lista_SQLite[3], lista_SQLite[4]))
curPostgres.execute("SELECT * FROM public.states")
lista_Postgres = curPostgres.fetchone()

print(lista_Postgres)