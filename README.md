# Azure AI Search Index - Implementação Prática

Projeto demonstrando a implementação de um índice de pesquisa usando Azure AI Search, incluindo ingestão de dados e consultas avançadas.

## 📌 Funcionalidades Principais

- Criação de índice de pesquisa
- Ingestão de documentos em formato JSON
- Consultas com syntax avançada
- Filtros e facets
- Integração com Python SDK

## 🛠️ Pré-requisitos

- Conta no [Microsoft Azure](https://azure.microsoft.com/)
- Serviço Azure AI Search provisionado
- Python 3.8+
- Azure CLI instalado

## 🔧 Passo a Passo

1. **Preparação**  
   ```bash
   cd projeto-azure-search
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   pip install azure-search-documents python-dotenv
   
