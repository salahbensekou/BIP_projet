import mysql.connector
import streamlit as st
from config import DB_CONFIG

def connect_to_db():
    try:
        cnx = mysql.connector.connect(**DB_CONFIG)
        return cnx
    except mysql.connector.Error as err:
        st.error(f"Erreur de connexion à MySQL : {err}")
        return None

def execute_query(cnx, sql_query):
    try:
        cursor = cnx.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return results, columns
    except mysql.connector.Error as err:
        st.error(f"Erreur SQL : {err}")
        return [], []
    finally:
        if cnx and cnx.is_connected():
            cursor.close()
