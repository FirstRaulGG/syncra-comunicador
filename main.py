import streamlit as st
import openai
import os

# Chave e ID do projeto
openai.api_key = "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"
openai.organization = "proj_U4f1vdKVNHOtArvxnDbhV1aj"

st.title("🧠 Copiloto de Comunicação para Assessores")
st.write("Ajuda assessores a responder clientes com clareza, segurança e em conformidade com a CVM.")

perfil = st.selectbox("Perfil do Cliente", ["Conservador", "Moderado", "Agressivo"])
pergunta = st.text_area("Pergunta ou Situação do Cliente")

if st.button("Gerar Resposta"):
    with st.spinner("Gerando resposta..."):
        prompt = f"Cliente com perfil {perfil.lower()} pergunta: {pergunta}\nResposta adequada, clara, segura e conforme com as regras da CVM:"
        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assessor financeiro experiente que responde clientes com clareza, segurança e em conformidade com a CVM."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.success(resposta['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"Erro: {e}")
