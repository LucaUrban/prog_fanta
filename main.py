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

session = st.session_state
session.CognomeVal = ""
session.RuoloVal = ""

#funzione estrazione casuale calciatore
def inserisciGiocatoreDataframe(df, ruolo, cognome, price):
    idx = min(df[df["Prezzo"] == 0].index)
    df.loc[idx, "Cognome"] = cognome
    st.write(cognome + "hrtbghr")
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

#costruzione dataframe giocatori
Alessandro = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Andrea = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Federico = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Gabriele = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Luca = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Michele = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Valerio = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])
Valter = pd.DataFrame(data[0]['Squadra'], columns = ["Ruolo", "Cognome", "Prezzo"])

#importazione lista calciatori
table = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/ListaGiocatori.CSV', delimiter = ";")

#Apllicazione
st.title("Applicazione Fanta")
if st.button('Estrai Giocatore'):
    giocatore = table.sample(n=1)
    table.drop(giocatore.index, axis = 0, inplace = True)
    table.reset_index(inplace=True)
    Ruolo = st.text_input("Ruolo giocatore", giocatore["ruolo"].values[0])
    Cognome = st.text_input("Cognome giocatore", giocatore["cognome"].values[0])
    Squadra = st.text_input("Squadra giocatore", giocatore["squadra"].values[0])
    session.CognomeVal = Cognome
    session.RuoloVal = Ruolo
st.write(session.CognomeVal)

colA, colB = st.columns(2, gap = "large")
with colA:
    acquirente = st.selectbox("Acquirente", ["Alessandro", "Andrea", "Gabriele", "Luca", "Michele", "Morto", "Valerio", "Valter"], 0)
with colB:
    prezzo = st.number_input("Prezzo", min_value=1, max_value=476, value=1)
if st.button('Registra acquisto'):
    if acquirente == "Alessandro":
        st.write(session.CognomeVal)
        inserisciGiocatoreDataframe(Alessandro, session.RuoloVal, session.CognomeVal, prezzo)
                

col1, col2, col3, col4 = st.columns(4, gap = "small")
with col1:
    st.write("Alessandro")
    st.dataframe(Alessandro, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Luca")
    st.dataframe(Luca, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col2:
    st.write("Andrea")
    st.dataframe(Andrea, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Michele")
    st.dataframe(Michele, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col3:
    st.write("Federico")
    st.dataframe(Federico, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Valerio")
    st.dataframe(Valerio, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col4:
    st.write("Gabriele")
    st.dataframe(Gabriele, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Valter")
    st.dataframe(Valter, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)

