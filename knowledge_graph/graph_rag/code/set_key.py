from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv, set_key
import os
# Load existing .env file
load_dotenv()

keyVaultName = "advait-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

def get_secret(client, secret_name):
    return client.get_secret(secret_name).value

OPENAI_API_KEY = get_secret(client, "OPENAI-API-KEY")

# Fetch the secret
secret_name = "GRAPHRAG_API_KEY"

# Update .env file with the fetched secret
# set_key(".env", secret_name, OPENAI_API_KEY)

print("Setting the env variables")
os.environ['GRAPHRAG_API_KEY'] = OPENAI_API_KEY
get_key = os.getenv("GRAPHRAG_API_KEY")
print(f"GRAPHRAG_API_KEY:{get_key}")

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
get_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY:{get_key}")

os.environ['GRAPHRAG_LLM_API_KEY'] = OPENAI_API_KEY 
get_key = os.getenv("GRAPHRAG_LLM_API_KEY")
print(f"GRAPHRAG_LLM_API_KEY:{get_key}")