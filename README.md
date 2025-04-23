🔍 Objectif : Ce projet vise à concevoir un système de Business Intelligence pour le secteur touristique de la région de Drâa-Tafilalet, permettant d’analyser les performances, de générer des visualisations dynamiques, et d’exploiter l’intelligence artificielle pour la prédiction et la recommandation.

🧱 Pipeline technique :

🚀 Intégration & Nettoyage avec Talend (ETL) :

Extraction des données depuis les sources Excel / CSV fournies par la Délégation du Tourisme.

Transformation et normalisation des données (dates, noms de villes, formats).

Chargement des données propres dans un Data Warehouse MySQL structuré en schéma en étoile.
![image](https://github.com/user-attachments/assets/19f0762f-59c8-42ec-84ad-fc155264ff56)


🗃️ Modélisation du Data Warehouse :

Table de faits : faits_hebergement (arrivées, nuitées…)

Tables de dimensions : dim_ville, dim_temps, dim_hebergement, dim_annee…
![image](https://github.com/user-attachments/assets/5aca054b-309b-4a2a-9e74-64ac88d341cf)

📊 Analyse & Visualisation :

Interface web interactive construite avec Streamlit.

Génération dynamique de tableaux de bord avec Plotly (barres, lignes, camembert, etc.)
![image](https://github.com/user-attachments/assets/46d8aee7-59af-43ce-b614-6cdaab31cad1)
![image](https://github.com/user-attachments/assets/65016820-a049-4005-b543-d5bbe060b202)
![image](https://github.com/user-attachments/assets/2875fbf8-cb4b-4429-ba12-d34e9ef3d44b)



Exploration visuelle assistée par requêtes SQL générées via un chatbot.

💬 Interaction avec LLM (IA) :
![image](https://github.com/user-attachments/assets/420f6f65-1894-431a-8b2e-040625879541)
![image](https://github.com/user-attachments/assets/39b12eea-a6e7-470f-9e64-8f1b366f7d7a)



Intégration d’un chatbot intelligent via Gemini/GPT pour comprendre les questions en langage naturel et générer automatiquement les requêtes SQL.

Exemple : “Combien de touristes en 2023 par ville ?” → Génère SQL → Affiche le graphique correspondant.

🤖 Perspectives IA :

Intégration prochaine de modèles de Machine Learning pour :

prédire les flux touristiques par ville et saison

recommander des activités ou offres selon les profils des visiteurs

Objectif : enrichir la prise de décision des responsables régionaux et hôteliers.

🧠 Technologies :

Talend Open Studio

MySQL

Streamlit + Plotly

LLM (Google Gemini ou GPT)

Pandas / Seaborn

VS-code

Python 3.11
