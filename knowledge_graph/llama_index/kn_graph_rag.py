# My OpenAI Key
import os
import logging
import sys
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex
from llama_index.core.graph_stores import SimpleGraphStore

from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
# from IPython.display import Markdown, display

#keyVaultName = os.environ["KEY_VAULT_NAME"]
keyVaultName = "advait-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

def get_secret(client, secret_name):
    return client.get_secret(secret_name).value

OPENAI_API_KEY = get_secret(client, "OPENAI-API-KEY")

print("Setting the env variables")
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

documents = SimpleDirectoryReader(
    "./docs"
).load_data()

# define LLM
# NOTE: at the time of demo, text-davinci-002 did not have rate-limit errors

llm = OpenAI(temperature=0, model="gpt-4o-2024-05-13")
Settings.llm = llm
Settings.chunk_size = 512

from llama_index.core import StorageContext

graph_store = SimpleGraphStore()
storage_context = StorageContext.from_defaults(graph_store=graph_store)

# NOTE: can take a while!
index = KnowledgeGraphIndex.from_documents(
    documents,
    max_triplets_per_chunk=2,
    storage_context=storage_context,
)


query_engine = index.as_query_engine(
    include_text=False, response_mode="tree_summarize"
)
response = query_engine.query(
    "Tell me more about Interleaf",
)
print(f"response:{response}")
# display(Markdown(f"{response}"))