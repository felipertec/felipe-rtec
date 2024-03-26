import streamlit as st
import pandas as pd
import numpy as np

st.write("Olá mundo, primeiro teste em Streamlit")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)