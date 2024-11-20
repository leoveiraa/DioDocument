from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalizeDocumentRequest
from ultils.config import config

def analyze_documente(card_url):
    try:
        credential = AzureKeyCredential(config.KEY)
        Document_Client = DocumentIntelligenceClient(config.ENDPOINT, credential)
        
        card-info = Document_Client.begin_analyze_document("prebuilt-creditCard", AnalizeDocumentRequest(url_source=card_url)
        

    return result
    except Exception as ex:
        return None