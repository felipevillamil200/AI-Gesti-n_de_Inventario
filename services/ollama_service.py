# services/ollama_service.py
import requests

OLLAMA_URL = 'http://localhost:11434/api/generate'

def ask_ollama(question, model_name, system_prompt):
    """
    Envía la pregunta del usuario al modelo Ollama y devuelve la respuesta.
    """
    prompt = f"""{system_prompt}

Pregunta del cliente: {question}
Respuesta:"""

    response = requests.post(OLLAMA_URL, json={
        "model": model_name,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json().get("response", "No se pudo generar una respuesta.")
    else:
        return "Error al comunicarse con el modelo."
