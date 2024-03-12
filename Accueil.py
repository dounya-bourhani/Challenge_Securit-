import streamlit as st
import pandas as pd

data = pd.read_csv("./attacks.csv", sep=',')
def main():
    

    st.title("Application Streamlit avec Onglets")

 

if __name__ == "__main__":
    main()
