import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

import streamlit as st
import pandas as pd
import plotly.express as px
from backend.database import connect_to_db, execute_query
from backend.llm_interface import generate_sql_query_with_gpt
from config import DB_SCHEMA

st.title("Chatbot d'Analyse des Hébergements (GPT)")

user_question = st.text_input("Posez votre question sur les données d'hébergement :")

cnx = connect_to_db()

if cnx:
    if user_question:
        st.info(f"Question : {user_question}")
        sql_query = generate_sql_query_with_gpt(user_question)
        st.code(sql_query, language="sql")

        if not sql_query.startswith("Erreur"):
            results, columns = execute_query(cnx, sql_query)

            if results:
                df = pd.DataFrame(results, columns=columns)
                st.subheader("Résultats :")
                st.dataframe(df)

                try:
                    if len(df) > 0:
                        if 'Nom_Region' in df.columns and 'Arrivees' in df.columns:
                            fig = px.bar(df, x='Nom_Region', y='Arrivees', title='Arrivées par Région')
                            st.plotly_chart(fig)
                        elif 'Annees' in df.columns and 'Nuitees' in df.columns:
                            fig = px.line(df, x='Annees', y='Nuitees', title='Évolution des Nuitées')
                            st.plotly_chart(fig)
                        elif len(df.columns) == 2 and pd.api.types.is_numeric_dtype(df.iloc[:, 1]):
                            fig = px.bar(df, x=df.columns[0], y=df.columns[1], title=f'{df.columns[1]} par {df.columns[0]}')
                            st.plotly_chart(fig)
                except Exception as e:
                    st.warning(f"Visualisation impossible : {e}")
            else:
                st.warning("Aucun résultat retourné.")
        else:
            st.error(sql_query)

    if cnx.is_connected():
        cnx.close()
else:
    st.error("Connexion à la base de données impossible.")
