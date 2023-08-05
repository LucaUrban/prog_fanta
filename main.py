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

#funzione estrazione casuale calciatore
def inserisciGiocatoreDataframe(df, giocatore, price):
    idx = min(df[df["Prezzo"] == 0].index)
    #df.loc[idx, "Cognome"] = giocatore[["cognome"]].values[0]
    st.write(giocatore)
    df.loc[idx, "Prezzo"] = price
    #st.write(df["Ruolo"][idx])

#funzione creazione excel
def createExcel():
    st.write("tdtdtufotf")

#importazione lista calciatori
table = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/ListaGiocatori.CSV', delimiter = ";")

#importazione csv partecipanti
Alessandro = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Alessandro.csv')
Andrea = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Andrea.csv')
Gabriele = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Gabriele.csv')
Luca = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Luca.csv')
Michele = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Michele.csv')
Morto = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Morto.csv')
Valerio = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Valerio.csv')
Valter = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/Valter.csv')

#Apllicazione
st.title("Applicazione Fanta")

if st.button('Estrai Giocatore'):
    giocatore = table.sample(n=1)
    table.drop(giocatore.index, axis = 0, inplace = True)
    table.reset_index(inplace=True)
    st.write(giocatore)

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
                inserisciGiocatoreDataframe(Alessandro, giocatore, prezzo)
                

col1, col2, col3, col4 = st.columns(4, gap = "small")
with col1:
    st.write("Alessandro")
    st.dataframe(Alessandro, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Michele")
    st.dataframe(Michele, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col2:
    st.write("Andrea")
    st.dataframe(Andrea, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Morto")
    st.dataframe(Morto, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col3:
    st.write("Gabriele")
    st.dataframe(Gabriele, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Valerio")
    st.dataframe(Valerio, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
with col4:
    st.write("Luca")
    st.dataframe(Luca, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)
    st.write("")
    st.write("Valter")
    st.dataframe(Valter, use_container_width = True, height = 915, column_config={"Ruolo": st.column_config.ImageColumn("Ruolo")}, hide_index = True)

