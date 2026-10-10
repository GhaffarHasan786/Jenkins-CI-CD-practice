import os

api_key = os.getenv('API_KEY', 'NOT_FOUND')
print("🐳 Docker Container is Running!")
print(f"🔑 Fetched Secret Key (Masked in Logs): {api_key[:4]}**")