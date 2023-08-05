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


st.title("Visual Information Quality Environment")

left, center, right = st.columns([0.4, 0.4, 0.2], gap = "large")
with left: 
    out_id_col = st.selectbox("Acquirente", ["Alessandro", "Andrea", "Gabriele", "Luca", "Michele", "Morto", "Valerio", "Valter"], 0)
with center:
    ch_out_type = st.number_input("Prezzo", min_value=1, max_value=476, value=1)
with right:
    colB1, colB2, colB3 = st.columns(3, gap = "large")
    with colB2:
        st.write("")
        st.button('Say hello')
