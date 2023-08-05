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

#functions
def estraiGiocatore(df):
    giocatore = df.sample(n=1)
    st.table(giocatore)
    

#importazione lista calciatori
table = pd.read_csv('https://raw.githubusercontent.com/LucaUrban/prog_fanta/main/fanta/ListaGiocatori.CSV', delimiter = ";")

#Titolo apllicazione
st.title("Applicazione Fanta")

left, center, right = st.columns(3, gap = "large")
with center:
    colB1, colB2, colB3 = st.columns([0.15, 0.7, 0.15], gap = "large")
    with colB2:
        if st.button('Estrai Giocatore'): estraiGiocatore(table)
    

left, center, right = st.columns([0.4, 0.4, 0.2], gap = "large")
with left: 
    acquirente = st.selectbox("Acquirente", ["Alessandro", "Andrea", "Gabriele", "Luca", "Michele", "Morto", "Valerio", "Valter"], 0)
with center:
    prezzo = st.number_input("Prezzo", min_value=1, max_value=476, value=1)
with right:
    colB1, colB2, colB3 = st.columns([0.15, 0.7, 0.15], gap = "large")
    with colB2:
        st.button('Registra acquisto')
