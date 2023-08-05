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

left, center, right = st.columns(3)
with left: 
    out_id_col = st.selectbox("Acquirente", ["Alessandro", "Andrea", "Gabriele", "Luca", "Michele", "Morto", "Valerio", "Valter"], 0)
with center:
    ch_out_type = st.number_input("Prezzo", min_value=1, max_value=476, value=1)
with right:
    st.write("")
    st.button('Say hello')
