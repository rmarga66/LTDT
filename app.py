import streamlit as st
import smtplib
from email.message import EmailMessage

# Fonction pour envoyer un email
def send_email(subject, body, to_email):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = "romainmargalet@gmail.com"
        msg["To"] = to_email

        # Configuration SMTP (vérifiez les paramètres de votre fournisseur de messagerie)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("romainmargalet@gmail.com", "oipm xjxx lyab obeq")  # Remplacez par votre mot de passe ou token
            smtp.send_message(msg)
    except Exception as e:
        st.error(f"Erreur lors de l'envoi de l'email : {e}")

# Titre et description de l'application
st.set_page_config(page_title="La Taula Del Temps", page_icon="⛅", layout="centered")
st.image("logo.png", caption="La Taula Del Temps", use_container_width=True)
st.title("La Taula Del Temps")
st.subheader("Demande d'invitation")

# Formulaire de saisie des données du guest
with st.form("guest_form"):
    st.write("Veuillez renseigner vos informations :")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    telephone = st.text_input("Téléphone")
    mail = st.text_input("Email")
    allergies = st.text_area("Allergies")
    autres = st.text_area("Autres informations")

    # Bouton pour soumettre
    submitted = st.form_submit_button("S'inscrire")

    if submitted:
        if not (nom and prenom and telephone and mail):
            st.error("Merci de remplir tous les champs obligatoires (Nom, Prénom, Téléphone, Email).")
        else:
            # Contenu de l'email
            email_subject = f"DEMANDE LTDT du GUEST {nom}"
            email_body = f"Informations du GUEST :\n\n" \
                         f"Nom : {nom}\n" \
                         f"Prénom : {prenom}\n" \
                         f"Téléphone : {telephone}\n" \
                         f"Email : {mail}\n" \
                         f"Allergies : {allergies}\n" \
                         f"Autres informations : {autres}\n\n" \
                         f"[Valider l'invitation](mailto:{mail}?subject=Reponse%20pour%20La%20Taula%20Del%20Temps&body=valider%20l'invitation) | " \
                         f"[Refuser l'invitation](mailto:{mail}?subject=Reponse%20pour%20La%20Taula%20Del%20Temps&body=Complet)"

            send_email(email_subject, email_body, "romainmargalet@gmail.com")
            st.success("Votre demande a été envoyée avec succès !")

# Style personnalisé pour une interface colorée
def apply_custom_styles():
    st.markdown(
        """
        <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: white;
            color: black;
            border: 2px solid #4CAF50;
        }
        .stApp {
            background: linear-gradient(to bottom right, #ff9800, #4caf50);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_styles()
