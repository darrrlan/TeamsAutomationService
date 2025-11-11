import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carrega as variáveis do arquivo .env
load_dotenv()

# 🔹 Azure AD / Microsoft Graph
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GRAPH_API_URL = os.getenv("GRAPH_API_URL", "https://graph.microsoft.com/v1.0")

# 🔹 MongoDB
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# Conexão com o MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def check_env():
    """Verifica se todas as variáveis essenciais estão definidas."""
    missing = [
        key for key, value in {
            "TENANT_ID": TENANT_ID,
            "CLIENT_ID": CLIENT_ID,
            "CLIENT_SECRET": CLIENT_SECRET,
            "MONGO_URI": MONGO_URI,
            "MONGO_DB_NAME": MONGO_DB_NAME,
        }.items() if not value
    ]
    if missing:
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")

check_env()

