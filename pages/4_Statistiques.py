import streamlit as st
import pandas as pd


# Chargement des données (assurez-vous d'adapter le chemin du fichier)
data = pd.read_csv("./attacks.csv", sep=',')



# Statistiques relatives
st.header("Statistiques relatives")
st.subheader("TOP 5 des IP sources les plus émettrices")
st.write(data['ipsrc'].value_counts().head(5))

# TOP 10 des ports inférieurs à 1024 avec un accès autorisé
allowed_ports_top10 = data[data['action'] == 'Permit'].loc[data['dstport'] < 1024, 'dstport'].value_counts().nlargest(10)
st.subheader("TOP 10 des ports inférieurs à 1024 avec un accès autorisé")
st.write(allowed_ports_top10)

# Statistiques relatives
st.header("Statistiques relatives")
st.subheader("TOP 5 des IP sources les plus émettrices")
st.write(data['ipsrc'].value_counts().head(5))

# TOP 10 des ports inférieurs à 1024 avec un accès autorisé
allowed_ports_top10 = data[data['action'] == 'Permit'].loc[data['dstport'] < 1024, 'dstport'].value_counts().nlargest(10)
st.subheader("TOP 10 des ports inférieurs à 1024 avec un accès autorisé")
st.write(allowed_ports_top10)


# Assurez-vous de définir university_ip_list
university_ip_list = []
non_university_ips = data[~data['ipsrc'].isin(university_ip_list)]
st.subheader("Accès des adresses non inclues dans le plan d’adressage de l’Université")
#st.dataframe(non_university_ips)
