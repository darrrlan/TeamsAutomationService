from auth import get_access_token
from config import db

if __name__ == "__main__":
    print("🔐 Solicitando token de acesso...")
    token = get_access_token()
    print("✅ Token gerado com sucesso!")
    print(token[:200] + "...")
    print("\n🗄️ Testando conexão com o MongoDB...")
    try:
        databases = db.client.list_database_names()
        print("✅ Conexão bem-sucedida!")
        print("📚 Bancos disponíveis:", databases)
    except Exception as e:
        print("❌ Erro ao conectar ao MongoDB:", e)
