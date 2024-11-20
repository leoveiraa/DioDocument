import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utilis.config import config

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection.string(config.AZURE_STORAGE_CONNECTION_STRING)
        
        blob_client = blob_service_client.get_blob_client(container=config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {ex}")
        return None