# pages/Analyse_par_protocole.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analyse par protocole")


st.header("Analyse par protocole")

data = pd.read_csv("./attacks.csv", sep=',')


selected_protocol = st.selectbox("Sélectionnez le protocole", data['proto'].unique())
# Sélection de l'action
selected_action = st.selectbox("Sélectionnez l'action", data['action'].unique())

# Filtrer les données en fonction du protocole et de l'action sélectionnés
filtered_data = data[(data['proto'] == selected_protocol) & (data['action'] == selected_action)]

# Filtrer les données par plages de ports
port_range = st.slider("Filtrer par plage de ports", min_value=0, max_value=65535, value=(0, 65535))

# Nettoyer les valeurs de la colonne ipsrc
filtered_data['ipsrc'] = filtered_data['ipsrc'].apply(lambda x: str(x).strip())  # Convertir en chaîne et supprimer les espaces
filtered_data['ipsrc'] = filtered_data['ipsrc'].replace('None', pd.NA)  # Remplacer 'None' par une valeur manquante

port_range = (int(port_range[0]), int(port_range[1]))

# Filtrer les données
filtered_data = filtered_data[
    # (filtered_data['PrtSrc'].between(port_range[0], port_range[1], inclusive='both')) |
    (filtered_data['ipsrc'].between(str(port_range[0]), str(port_range[1]), inclusive='both'))
]

# Ajouter la représentation graphique (graphique de dispersion)
st.write(f"Flux {selected_protocol}")
st.dataframe(filtered_data)

fig_scatter = px.scatter(filtered_data, x='ipsrc', y='dstport', color='action', title=f'Flux {selected_protocol}')
st.plotly_chart(fig_scatter)

# Ajouter une analyse temporelle
st.subheader("Analyse temporelle")

# Convertir la colonne 'date' en format datetime si ce n'est pas déjà le cas
filtered_data['datetime'] = pd.to_datetime(filtered_data['datetime'])

    # Créer un graphique temporel interactif avec une ligne
fig_temporal = px.line(filtered_data, x='datetime', y='dstport', color='action', title=f'Analyse Temporelle - Flux {selected_protocol}')
st.plotly_chart(fig_temporal)
