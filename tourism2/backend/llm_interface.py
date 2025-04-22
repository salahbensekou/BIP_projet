import requests
from config import OPENAI_API_KEY, DB_SCHEMA

def generate_sql_query_with_gpt(question):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  # tu peux tester aussi : "google/gemini-pro", "anthropic/claude-3-haiku", etc.
        "messages": [
            {"role": "system", "content": "Tu es un expert SQL."},
            {"role": "user", "content": f"""
Voici le schéma de la base :
{DB_SCHEMA}

Génère une requête SQL pour répondre à cette question :
"{question}"

Donne uniquement la requête SQL, sans explication ni formatage.
"""}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"].strip()
        else:
            return f"Erreur API OpenRouter : {data}"
    except Exception as e:
        return f"Erreur de requête : {e}"
