import requests
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

    payload = {
        'client_id': CLIENT_ID,
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        token = response.json().get("access_token")
        print("✅ Token obtido com sucesso!")
        return token
    else:
        print("❌ Erro ao obter token:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    get_access_token()
