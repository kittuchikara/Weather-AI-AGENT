import os
from dotenv import load_dotenv
from dataclasses import dataclass
from groq import Groq

load_dotenv()

@dataclass
class Provider:
    name: str
    env_var: str 
    is_free: bool 
    base_url: str | None 
    model: str

PROVIDERS = [
    Provider("Groq",       "GROQ_API_KEY",       True,  "https://api.groq.com/openai/v1", "qwen/qwen3.8-27b")
]

def select_provider()->Provider:
    for provider in PROVIDERS:
        print("Checking provider:", provider.name)
        print("Environment variable:", provider.env_var)
        print("Key loaded:", bool(os.getenv(provider.env_var)))
        if os.getenv(provider.env_var):
            return provider

    raise RuntimeError(f"No provider found")

def get_client_and_model() -> tuple[Groq, str, Provider]:
    provider=select_provider()
    api_key=os.getenv(provider.env_var)
    client=Groq(api_key=api_key)
    return client, provider.model, provider
