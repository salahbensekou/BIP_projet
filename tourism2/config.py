import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST') or 'localhost',
    'user': os.getenv('DB_USER') or 'salah',
    'password': os.getenv('DB_PASSWORD') or '2001',
    'database': os.getenv('DB_DATABASE') or 'dwh_orion'
}

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or ''

DB_SCHEMA = """
Tables:
faits_hebergement (id_fait INT, id_ville INT, id_annee INT, id_category INT, Arrivees INT, Nuitees INT),
dim_region (id_region INT, Nom_Region VARCHAR(255)),
dim_ville (id_ville INT, Ville VARCHAR(255), id_region INT),
dim_annee (id_annee INT, Annees INT),
dim_category (id_category INT, Category VARCHAR(255), id_type_hebergement INT),
dim_type_hebergement (id_type_hebergement INT, Type_Hebergement VARCHAR(255))

Relations (clés étrangères) :
faits_hebergement.id_ville -> dim_ville.id_ville
faits_hebergement.id_annee -> dim_annee.id_annee
faits_hebergement.id_category -> dim_category.id_category
dim_ville.id_region -> dim_region.id_region
dim_category.id_type_hebergement -> dim_type_hebergement.id_type_hebergement
"""
