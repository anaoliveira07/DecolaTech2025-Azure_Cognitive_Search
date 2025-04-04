import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

load_dotenv()


service_name = os.getenv("AZURE_SEARCH_SERVICE_NAME")
admin_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
endpoint = f"https://{service_name}.search.windows.net"


credential = AzureKeyCredential(admin_key)
client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)

def run_queries():
    
    print("\n=== Busca por 'tecnologia' ===")
    results = client.search(search_text="tecnologia")
    for result in results:
        print(f"{result['title']} ({result['category']})")

    
    print("\n=== Documentos de Ciência ===")
    results = client.search(
        search_text="*",
        filter="category eq 'Ciência'",
        select=["title", "publish_date"]
    )
    for result in results:
        print(f"{result['title']} - {result['publish_date']}")

if __name__ == "__main__":
    run_queries()
