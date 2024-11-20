import streamlit as st
from services.blob_services import upload_blob

from services.blob_service import upload_blob

print("Importação bem-sucedida!")

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure Fake Docs")
    upload_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if upload_file is not None:
        fileName = upload_file.name

    blob_url = upload_blob(upload_file, fileName)
    if blob_url:
        st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
        credit_card_info = ""
        show_image_and_validation(blob_url, credit_card_info)
    else:
        st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação")
    if credit_card_info and "card_name" in credit_card_info:
        st.markdown(
            f"<h1 style='color: green;'>Cartão Válido</h1>", 
            unsafe_allow_html=True
        )
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(
            f"<h1 style='color: red;'>Cartão Inválido</h1>", 
            unsafe_allow_html=True
        )
        st.write("Este não é um cartão de crédito válido.")
        
if __name__ == "__main__":
    configure_interface()
