import streamlit as st
st.set_page_config(page_title="Assistant IA Chirurgie", layout="centered")

from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

# Chargement du modèle fine-tuné
@st.cache_resource
def load_model():
    model = AutoModelForQuestionAnswering.from_pretrained("my_qa_model")
    tokenizer = AutoTokenizer.from_pretrained("my_qa_model")
    return pipeline("question-answering", model=model, tokenizer=tokenizer)

qa_pipeline = load_model()

# Fonction pour classer la réponse
def classer_reponse(score, reponse):
    reponse = reponse.lower().strip()
    if score < 0.2 or reponse in ["", "n/a", "unknown"]:
        return "Inconnu"
    elif any(neg in reponse for neg in ["no", "not", "none", "tolerated", "without", "denies", "free of"]):
        return "Non"
    else:
        return "Oui"

# Interface utilisateur 
st.title("💬 Assistant Clinique IA - Chirurgie")

# Input utilisateur
question = st.text_input("❓ Question clinique :", placeholder="e.g. Is the patient anticoagulated?")
context = st.text_area("📄 Texte médical :", height=250, placeholder="e.g. The patient is currently on anticoagulants...")

if st.button("🔍 Interroger le modèle") and question and context:
    with st.spinner("Traitement en cours..."):
        result = qa_pipeline(question=question, context=context)
        score = round(result['score'], 3)
        reponse = result['answer']
        label = classer_reponse(score, reponse)

        st.success("✅ Réponse obtenue !")
        st.markdown(f"**🧠 Réponse (Oui / Non / Inconnu) :** {label}")
        st.markdown(f"**📊 Score de confiance :** {round(score * 100, 2)} %")

        start = result['start']
        end = result['end']
        highlighted = (
        context[:start]
        + f"<mark style='background-color: #ffeb3b; padding: 2px 4px; border-radius: 4px;'>{context[start:end]}</mark>"
        + context[end:]
             )
        st.markdown("**🔎 Extrait trouvé dans le texte :**", unsafe_allow_html=True)
        st.markdown(highlighted, unsafe_allow_html=True)

