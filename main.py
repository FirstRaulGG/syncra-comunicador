import streamlit as st
import openai
import os

# Chave e ID do projeto (chave diretamente no código — menos seguro, apenas para testes)
openai.api_key = "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"
openai.organization = "proj_U4f1vdKVNH0tArvxnDbhV1aj"

st.set_page_config(page_title="Copiloto de Comunicação para Assessores", page_icon="🧠")
st.title("🧠 Copiloto de Comunicação para Assessores")
st.write("Ajuda assessores a responder clientes com clareza, segurança e em conformidade com a CVM.")

perfil = st.selectbox("Perfil do Cliente", ["Conservador", "Moderado", "Agressivo"])
pergunta = st.text_area("Pergunta ou Situação do Cliente")

if st.button("Gerar Resposta"):
    with st.spinner("Gerando resposta..."):
        try:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": f"Você é um assessor financeiro experiente que responde clientes com clareza, segurança e em conformidade com a CVM. Perfil do cliente: {perfil}"},
                    {"role": "user", "content": pergunta}
                ]
            )
            resposta = response.choices[0].message.content
            st.success("Resposta gerada com sucesso!")
            st.markdown("### 🧠 Resposta sugerida:")
            st.write(resposta)
        except Exception as e:
            st.error(f"Erro: {e}")
