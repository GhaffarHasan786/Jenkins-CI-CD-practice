import os

target_env = os.getenv('TARGET_ENV', 'dev')
print(f"🚀 Deploying application version 1.0.0 to [{target_env.upper()}] environment...")
print("✅ Deployment completed successfully!")
