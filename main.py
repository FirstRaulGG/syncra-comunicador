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
            resposta = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": f"Você é um assessor financeiro experiente que responde clientes com clareza, segurança e em conformidade com a CVM. O perfil do cliente é {perfil}."},
                    {"role": "user", "content": pergunta}
                ]
            )
            resposta_final = resposta.choices[0].message.content
            st.success("✅ Resposta gerada com sucesso!")
            st.markdown("### 🧠 Resposta sugerida:")
            st.write(resposta_final)

        except Exception as e:
            st.error(f"Erro: {e}")
