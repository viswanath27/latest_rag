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
from llama_index.core import StorageContext
# from IPython.display import Markdown, display

keyVaultName = "advait-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

def get_secret(client, secret_name):
    return client.get_secret(secret_name).value

print("Fetching the keys from vault")
OPENAI_API_KEY = get_secret(client, "OPENAI-API-KEY")

print("setting the requried env variables")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
print("Load the data in this case text file")
documents = SimpleDirectoryReader(
    "../data"
).load_data()

# define LLM
# NOTE: at the time of demo, text-davinci-002 did not have rate-limit errors
print("Initialize the model, in this case gpt 4o")
llm = OpenAI(temperature=0, model="gpt-4o-2024-05-13")
Settings.llm = llm
Settings.chunk_size = 512


print("Instantiate the graph store")
graph_store = SimpleGraphStore()
storage_context = StorageContext.from_defaults(graph_store=graph_store)

print("Index the data, create the knowledge graph")
# NOTE: can take a while!
index = KnowledgeGraphIndex.from_documents(
    documents,
    max_triplets_per_chunk=2,
    storage_context=storage_context,
)
print("Instantiate the query engine")
query_engine = index.as_query_engine(
    include_text=False, response_mode="tree_summarize"
)
print("Ask a question and get response")

print("Question in this case is : Tell me more about Interleaf")

response = query_engine.query(
    "Tell me more about Interleaf",
)
print(f"response:{response}")