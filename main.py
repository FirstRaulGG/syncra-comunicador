import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar chave da API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Syncra - Copiloto de Comunicação", page_icon="🤖")
st.title("🤖 Copiloto de Comunicação para Assessores")
st.markdown("Ajuda assessores a responder clientes com clareza, segurança e em conformidade com a CVM.")

# Inputs do usuário
perfil_cliente = st.selectbox("Perfil do Cliente", ["Conservador", "Moderado", "Agressivo"])
pergunta = st.text_area("Pergunta ou Situação do Cliente", height=150, placeholder="Ex: Cliente conservador quer sair da bolsa após queda...")

if st.button("Gerar Resposta") and pergunta:
    with st.spinner("Gerando resposta..."):
        try:
            system_prompt = f"""
Você é um copiloto de comunicação para assessores de investimentos no Brasil.
Sua função é ajudar a explicar decisões financeiras de forma clara, segura e sem prometer retornos.
Sempre respeite o perfil do cliente: {perfil_cliente}.
Use linguagem simples, mostre os riscos envolvidos e mantenha conformidade com as normas da CVM.
Gere também uma versão adaptada para WhatsApp.
"""

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": pergunta}
                ],
                max_tokens=800,
                temperature=0.7
            )

            output = response.choices[0].message.content
            st.success("✅ Resposta gerada com sucesso!")
            st.markdown("### 🧠 Resposta sugerida:")
            st.write(output)

        except Exception as e:
            st.error(f"Erro: {e}")

st.markdown("---")
st.caption("Syncra MVP – v0.1")
