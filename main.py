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
