import streamlit as st
import openai

# Use diretamente sua chave válida
openai.api_key = "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"

st.set_page_config(page_title="Copiloto de Comunicação para Assessores", page_icon="🧠")
st.title("🧠 Copiloto de Comunicação para Assessores")
st.write("Ajuda assessores a responder clientes com clareza, segurança e em conformidade com a CVM.")

perfil = st.selectbox("Perfil do Cliente", ["Conservador", "Moderado", "Agressivo"])
pergunta = st.text_area("Pergunta ou Situação do Cliente")

if st.button("Gerar Resposta") and pergunta:
    with st.spinner("Gerando resposta..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": f"Você é um assessor financeiro experiente que responde clientes com clareza, segurança e em conformidade com a CVM. O perfil do cliente é {perfil}."},
                    {"role": "user", "content": pergunta}
                ]
            )
            resposta = response.choices[0].message.content
            st.success("✅ Resposta gerada com sucesso!")
            st.markdown("### 💬 Resposta sugerida:")
            st.write(resposta)
        except Exception as e:
            st.error(f"Erro: {e}")
