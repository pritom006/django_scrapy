import requests

OLLAMA_URL = "http://localhost:11434/api"

def interact_with_ollama(model: str, prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/{model}",
        json={"prompt": prompt}
    )
    response.raise_for_status()
    return response.json()["response"]
