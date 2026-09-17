import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculateur de Thème Numérologique - MR Coaching",
    page_icon="✨",
    layout="centered"
)

# Fonctions de calcul numérologique
def reduire(nombre):
    while nombre > 9 and nombre not in [11, 22, 33]:
        nombre = sum(int(chiffre) for chiffre in str(nombre))
    return nombre

def calcul_lettre(lettre):
    lettre = lettre.upper()
    table = {
        'A': 1, 'J': 1, 'S': 1,
        'B': 2, 'K': 2, 'T': 2,
        'C': 3, 'L': 3, 'U': 3,
        'D': 4, 'M': 4, 'V': 4,
        'E': 5, 'N': 5, 'W': 5,
        'F': 6, 'O': 6, 'X': 6,
        'G': 7, 'P': 7, 'Y': 7,
        'H': 8, 'Q': 8, 'Z': 8,
        'I': 9, 'R': 9
    }
    return table.get(lettre, 0)

def calculer_nom(texte):
    texte_nettoye = "".join(c for c in texte if c.isalpha())
    somme = sum(calcul_lettre(c) for c in texte_nettoye)
    return somme, reduire(somme)

# --- INTERFACE STREAMLIT ---
st.title("✨ Calculateur de Thème Numérologique ✨")
st.markdown("Remplis les informations ci-dessous pour découvrir ton thème numérologique personnalisé.")

with st.form("formulaire_theme"):
    tous_les_prenoms = st.text_input("Tous les prénoms de naissance (ex: Matthieu Louis Philippe Marie)", placeholder="Sépare tes prénoms par un espace")
    nom_famille = st.text_input("Nom de famille", placeholder="Ex: Rubino")
    date_naissance = st.text_input("Date de naissance (JJ/MM/AAAA)", placeholder="Ex: 24/10/2001")
    
    submit_button = st.form_submit_button(label="Calculer mon Thème")

if submit_button:
    if not tous_les_prenoms or not nom_famille or not date_naissance:
        st.error("⚠️ Veuillez remplir tous les champs du formulaire.")
    else:
        # Traitement prénoms
        liste_prenoms = tous_les_prenoms.strip().split()
        prenom_usuel = liste_prenoms[0] if liste_prenoms else ""

        # Calculs
        somme_simple, expr_simple = calculer_nom(prenom_usuel + nom_famille)
        somme_complet, expr_complet = calculer_nom(tous_les_prenoms + nom_famille)
        
        chiffres_date = [int(c) for c in date_naissance if c.isdigit()]
        somme_cv = sum(chiffres_date)
        chemin_vie = reduire(somme_cv)
        
        parties = date_naissance.split('/')
        
        if len(parties) == 3:
            try:
                jour = int(parties[0])
                mois = int(parties[1])
                somme_mv = jour + mois
                mission_vie = reduire(somme_mv)
                
                annee_universelle = 2026
                somme_ap = sum(int(c) for c in str(jour)) + sum(int(c) for c in str(mois)) + sum(int(c) for c in str(annee_universelle))
                annee_perso = reduire(somme_ap)
                
                mois_actuel = 9
                somme_mp = annee_perso + mois_actuel
                mois_perso = reduire(somme_mp)
                
                # --- AFFICHAGE DES RÉSULTATS EN BLOCS DESIGN ---
                st.success("🎯 Thème calculé avec succès !")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label=f"Expression Simple ({prenom_usuel} {nom_famille})", value=expr_simple, delta=f"Somme: {somme_simple}")
                    st.metric(label=f"Chemin de Vie ({date_naissance})", value=chemin_vie, delta=f"Somme: {somme_cv}")
                    st.metric(label="Année Personnelle (2026)", value=annee_perso)
                with col2:
                    st.metric(label=f"Expression Complet", value=expr_complet, delta=f"Somme: {somme_complet}")
                    st.metric(label="Mission de Vie (Jour + Mois)", value=mission_vie, delta=f"Somme: {somme_mv}")
                    st.metric(label="Mois Personnel (Septembre)", value=mois_perso)
                    
            except ValueError:
                st.error("⚠️ Erreur : Le format de la date de naissance n'est pas valide (utiliser le format JJ/MM/AAAA).")
        else:
            st.error("⚠️ Erreur : Le format de la date de naissance n'est pas valide (utiliser le format JJ/MM/AAAA).")

# --- PIED DE PAGE SIGNÉ ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #718096; font-size: 0.9em;'>"
    "Outil développé sur mesure par <b>MR Coaching</b>"
    "</div>", 
    unsafe_allow_html=True
)
