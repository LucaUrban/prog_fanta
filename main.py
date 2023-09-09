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
from json import loads, dumps

#funzione estrazione casuale calciatore
def inserisciGiocatoreDataframe(df, partecipante, ruolo, cognome, price):
    idx = min(df[(df["Prezzo"] == 0) & (df["Ruolo"].str.contains(ruolo))].index)
    df.loc[idx, "Cognome"] = cognome
    df.loc[idx, "Prezzo"] = price
    collection = client["Fantacalcio"]["Squadre"]
    collection.find_one_and_update({"Partecipante": partecipante}, {"$set": {"Squadra": loads(df.to_json(orient="records"))}})

#crea la tabella riassuntiva delle spese per un singolo partecipante
def creaTabRiassuntivaSpese(df, crediti_rimanenti):
    return pd.DataFrame([sum(df[df["Ruolo"].str.contains("P")]["Prezzo"].values), sum(df[df["Ruolo"].str.contains("D")]["Prezzo"].values), sum(df[df["Ruolo"].str.contains("C")]["Prezzo"].values),
                         sum(df[df["Ruolo"].str.contains("A")]["Prezzo"].values), crediti_rimanenti - sum(df["Prezzo"].values), (crediti_rimanenti+1) - sum(df["Prezzo"].values) - len(df[df["Prezzo"] == 0]["Prezzo"].values)],
                         columns = ["Crediti"], index = ["Cr. Portieri", "Cr. Difensori", "Cr. Centrocampisti", "Cr. Attaccanti", "Cr. Rimanenti", "Cr. Max Spendibili"])

# Connection to the cluster
@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://Fanta:fanta@fanta.3dy3ftn.mongodb.net/")

client = init_connection()

# Pull data from the collection.
def get_data():
    items = list(client["Fantacalcio"]["Squadre"].find())  # make hashable for st.cache_data
    return items

data = get_data()
session = st.session_state

#creazione dizionario crediti rimanenti
dict_crediti_rim = {item["Partecipante"]: item["crediti_rimanenti"] for item in data}

#costruzione dataframe giocatori
Alessandro = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Alessandro")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Andrea = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Andrea")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Federico = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Federico")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Gabriele = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Gabriele")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Luca = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Luca")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Michele = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Michele")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Valerio = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Valerio")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])
Valter = pd.DataFrame(next(item for item in data if item["Partecipante"] == "Valter")["Squadra"], columns = ["Ruolo", "Cognome", "Prezzo"])

#importazione lista calciatori
listaGiocatori = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/ListaGiocatori.CSV', delimiter = ";")

#Apllicazione
st.title("Applicazione Fanta")
Cognome = st.selectbox("Cognome giocatore", listaGiocatori["cognome"], key = "cognome")
Ruolo = st.text_input("Ruolo giocatore", listaGiocatori[listaGiocatori["cognome"] == Cognome]["ruolo"].values[0], key = "ruolo")

colA, colB = st.columns(2, gap = "large")
with colA:
    acquirente = st.selectbox("Acquirente", ["Alessandro", "Andrea", "Federico", "Gabriele", "Luca", "Michele", "Valerio", "Valter"], 0)
with colB:
    prezzo = st.number_input("Prezzo", min_value=1, max_value=476, value=1)
if st.button('Registra acquisto'):
    if acquirente == "Alessandro":
        inserisciGiocatoreDataframe(Alessandro, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Andrea":
        inserisciGiocatoreDataframe(Andrea, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Federico":
        inserisciGiocatoreDataframe(Federico, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Gabriele":
        inserisciGiocatoreDataframe(Gabriele, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Luca":
        inserisciGiocatoreDataframe(Luca, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Michele":
        inserisciGiocatoreDataframe(Michele, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Valerio":
        inserisciGiocatoreDataframe(Valerio, acquirente, Ruolo, Cognome, prezzo)
    if acquirente == "Valter":
        inserisciGiocatoreDataframe(Valter, acquirente, Ruolo, Cognome, prezzo)                

col1, col2, col3, col4 = st.columns(4, gap = "small")
with col1:
    st.write("Alessandro")
    st.dataframe(Alessandro, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Alessandro, dict_crediti_rim["Alessandro"]))
    st.write("")
    st.write("Luca")
    st.dataframe(Luca, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Luca, dict_crediti_rim["Luca"]))
with col2:
    st.write("Andrea")
    st.dataframe(Andrea, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Andrea, dict_crediti_rim["Andrea"]))
    st.write("")
    st.write("Michele")
    st.dataframe(Michele, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Michele, dict_crediti_rim["Michele"]))
with col3:
    st.write("Federico")
    st.dataframe(Federico, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Federico, dict_crediti_rim["Federico"]))
    st.write("")
    st.write("Valerio")
    st.dataframe(Valerio, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Valerio, dict_crediti_rim["Valerio"]))
with col4:
    st.write("Gabriele")
    st.dataframe(Gabriele, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Gabriele, dict_crediti_rim["Gabriele"]))
    st.write("")
    st.write("Valter")
    st.dataframe(Valter, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.table(creaTabRiassuntivaSpese(Valter, dict_crediti_rim["Valter"]))

