import streamlit as st
import pandas as pd
import plotly.express as px


# Chargement des données (assurez-vous d'adapter le chemin du fichier)
data = pd.read_csv("C:/Users/ndieng1/Documents/Challenge-secu/new-logs.csv", sep=',')

st.header("Visualisation interactive des données")
source_ip_counts = data['ipSrc'].value_counts()
selected_source_ip = st.selectbox("Sélectionnez une adresse IP source", source_ip_counts.index)

# Filtrer les données pour l'adresse IP sélectionnée
selected_ip_data = data[data['ipSrc'] == selected_source_ip]

# Afficher la représentation graphique interactive
fig_ip = px.bar(selected_ip_data, x='ipDest', color='action', title=f'Occurrences de destinations pour {selected_source_ip}')
st.plotly_chart(fig_ip)


# Utilisation de Plotly Express pour créer un histogramme avec des couleurs spécifiques
fig_protocol_distribution = px.histogram(data, x='Prot', color_discrete_sequence=['deepskyblue', 'dodgerblue'],
                                            title="Histogramme de la Répartition des Protocoles")

# Affichage de l'histogramme
st.plotly_chart(fig_protocol_distribution)

# Graphique de réseau (Network graph)
st.subheader("Graphique de réseau (Network graph)")

    
    # Création d'un graphique réseau avec NetworkX
    #G = nx.from_pandas_edgelist(data, source='ipsrc', target='ipdst', edge_attr='portdst')

    # Disposition du graphique avec Graphviz (à adapter selon vos besoins)
    #pos = graphviz_layout(G, prog="neato")

    # Affichage du graphique
    #fig, ax = plt.subplots(figsize=(10, 8))
    #nx.draw(G, pos, with_labels=True, font_size=8, node_size=100, font_color='black', node_color='lightblue', font_weight='bold', edge_color='gray')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['portdst']}" for u, v, d in G.edges(data=True)})

    #st.pyplot(fig)