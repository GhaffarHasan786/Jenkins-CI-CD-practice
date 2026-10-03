
import os

app_name = os.getenv('APP_NAME', 'DefaultApp')
env_type = os.getenv('DEPLOY_ENV', 'local')

print(f"=== Running {app_name} in {env_type} Environment ===")
print("Processing application Successfully...")


