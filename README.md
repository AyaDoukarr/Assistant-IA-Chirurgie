# 🧠 Assistant Clinique IA – Chirurgie  

Ce projet est né d’une idée simple : utiliser l’intelligence artificielle pour **aider les médecins, étudiants et chercheurs en chirurgie** à analyser plus facilement les textes médicaux.  

J’ai créé cette application avec **Streamlit** et un modèle de **question-réponse basé sur Transformers** (Hugging Face).  
L’idée, c’est de pouvoir poser une **question clinique** en langage naturel et de laisser le modèle trouver la réponse directement dans un texte médical.  

Par exemple :  
> ❓ *Le patient est-il anticoagulé ?*  
> 🧾 *Texte : Le patient est actuellement sous traitement anticoagulant oral...*  

L’application comprend la question, lit le texte et renvoie une réponse claire :  
**Oui**, **Non** ou **Inconnu**, accompagnée d’un **score de confiance** et d’un **extrait surligné** pour montrer d’où vient la réponse.  

C’est un petit assistant conçu pour rendre l’analyse de documents médicaux plus rapide, plus intuitive et plus interactive.  

---

## ⚙️ Fonctionnement  

1. Tu entres ta **question clinique**.  
2. Tu colles ton **texte médical** (extrait de compte rendu, observation, etc.).  
3. L’IA lit et comprend le texte.  
4. Elle te donne :  
   - Une réponse (Oui / Non / Inconnu)  
   - Un score de confiance (%)  
   - Le passage exact du texte surligné.  

Le tout fonctionne directement depuis ton navigateur grâce à **Streamlit**.  

---

## 🧩 Technologies utilisées  

- **Python**  
- **Streamlit** pour l’interface web  
- **Transformers (Hugging Face)** pour le modèle IA  
- **PyTorch** pour l’inférence du modèle  
- Un modèle personnalisé `my_qa_model` fine-tuné pour les textes médicaux.  

---

## 🚀 Installation  

```bash
# 1. Cloner le dépôt
git clone https://github.com/<ton-nom-utilisateur>/<nom-du-repo>.git
cd "<nom-du-repo>"

# 2. Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l’application
streamlit run app.py

