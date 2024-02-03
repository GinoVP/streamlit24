import streamlit as st 

import pandas as pd 

import numpy as np

from datetime import time


st.title('UPC Data Science 2024')

st.header('Simulador Ventas')

n = st.slider("cant. ventas", 5,100, step=1)

chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])

st.line_chart(chart_data)

d = st.date_input(
 "Fecha de cumpleaños",
 datetime.date(2023, 7, 6))
st.write('Tu cumpleños es:', d)

