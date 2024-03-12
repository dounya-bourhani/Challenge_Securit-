import streamlit as st
import pandas as pd


st.header("Page Données")
# Ajoutez le contenu spécifique de la page ici
#st.set_option('server.maxMessageSize', 500)  # Modifiez la valeur selon vos besoins

# Chargement des données (assurez-vous d'adapter le chemin du fichier)
data = pd.read_csv("C:/Users/ndieng1/Documents/Challenge-secu/new-logs.csv", sep=',')

# Affichage des données
st.dataframe(data)