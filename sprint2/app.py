import streamlit as st
import google.genai as genai # Atualizado para a versão correta da SDK

# Puxa a função de inteligência e os datasets do arquivo bot.py
from bot import responder_usuario

# Configuração da página do chat
st.set_page_config(page_title="Guia Técnico GoodWe", page_icon="🤖")
st.title("🤖 Guia Técnico GoodWe - ChargeGrid Intelligence")
st.markdown("---")

# Inicializa o histórico de mensagens se ele não existir
if "historico" not in st.session_state:
    st.session_state.historico = []

# Exibe as mensagens anteriores na tela (mantém o chat contínuo)
for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# Campo de entrada de texto para o usuário digitar
if pronto := st.chat_input("Digite sua dúvida técnica..."):
    # Exibe a pergunta do usuário no chat
    with st.chat_message("user"):
        st.markdown(pronto)
    st.session_state.historico.append({"role": "user", "content": pronto})

    # Envia a pergunta para o cérebro do Gemini no bot.py de forma segura
    try:
        resposta_da_ia = responder_usuario(pronto)
    except Exception as e:
        # Se algo der muito errado no bot.py, mostra um erro amigável em vez da tela vermelha
        resposta_da_ia = f"❌ Ocorreu um erro ao processar sua mensagem: {str(e)}"

    # Exibe a resposta do chatbot na tela
    with st.chat_message("assistant"):
        st.markdown(resposta_da_ia)
    st.session_state.historico.append({"role": "assistant", "content": resposta_da_ia})