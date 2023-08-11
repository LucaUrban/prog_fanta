import streamlit as st
import time
import base64
import os
from urllib.parse import quote as urlquote
from urllib.request import urlopen
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
import random
import csv
import pymongo

#funzione estrazione casuale calciatore
def inserisciGiocatoreDataframe(id, cognome, price):
    idx = min(df[df["Prezzo"] == 0].index)
    df.loc[idx, "Cognome"] = cognome
    st.write(cognome)
    df.loc[idx, "Prezzo"] = price

#funzione creazione excel
def createExcel():
    st.write("tdtdtufotf")

# Connection to the cluster
@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://Fanta:fanta@fanta.3dy3ftn.mongodb.net/")

client = init_connection()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    items = list(client["Fantacalcio"]["Squadre"].find())  # make hashable for st.cache_data
    return items

data = get_data()

#importazione lista calciatori
table = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/ListaGiocatori.CSV', delimiter = ";")

#Apllicazione
st.title("Applicazione Fanta")
placeholderRuolo = st.empty()
placeholderCognome = st.empty()
placeholderSquadra = st.empty()
Ruolo = placeholderRuolo.text_input("Ruolo giocatore", "")
Cognome = placeholderCognome.text_input("Cognome giocatore", "")
Squadra = placeholderSquadra.text_input("Squadra giocatore", "")
if st.button('Estrai Giocatore'):
    giocatore = table.sample(n=1)
    table.drop(giocatore.index, axis = 0, inplace = True)
    table.reset_index(inplace=True)
    Ruolo = placeholderRuolo.text_input("Ruolo giocatore", giocatore["ruolo"].values[0])
    Cognome = placeholderCognome.text_input("Cognome giocatore", giocatore["cognome"].values[0])
    Squadra = placeholderSquadra.text_input("Squadra giocatore", giocatore["squadra"].values[0])


left, center, right = st.columns([0.4, 0.4, 0.2], gap = "large")
with left: 
    acquirente = st.selectbox("Acquirente", ["Alessandro", "Andrea", "Gabriele", "Luca", "Michele", "Morto", "Valerio", "Valter"], 0)
with center:
    prezzo = st.number_input("Prezzo", min_value=1, max_value=476, value=1)
with right:
    colB1, colB2, colB3 = st.columns([0.15, 0.7, 0.15], gap = "large")
    with colB2:
        if st.button('Registra acquisto'):
            if acquirente == "Alessandro":
                inserisciGiocatoreDataframe(0, Cognome, prezzo)
                

col1, col2, col3, col4 = st.columns(4, gap = "small")
with col1:
    st.write("Alessandro")
    st.dataframe(pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Michele")
    st.dataframe(pd.DataFrame(data[4]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col2:
    st.write("Andrea")
    st.dataframe(pd.DataFrame(data[1]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Morto")
    st.dataframe(pd.DataFrame(data[5]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col3:
    st.write("Gabriele")
    st.dataframe(pd.DataFrame(data[2]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Valerio")
    st.dataframe(pd.DataFrame(data[6]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col4:
    st.write("Luca")
    st.dataframe(pd.DataFrame(data[3]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Valter")
    st.dataframe(pd.DataFrame(data[7]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"]), use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)

