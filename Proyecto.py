import streamlit as st 

import pandas as pd 

import numpy as np

from datetime import time

import datetime

st.title('UPC Data Science 2024')

st.header('Simulador Ventas')

n = st.slider("cant. ventas", 5,100, step=1)

chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])

st.line_chart(chart_data)

df = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])

option = st.selectbox(
 '¿Cómo desearía ser contactado/a?',
 ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)


d = st.date_input(
 "Fecha de cumpleaños",
 datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)

start_time = st.slider(
 "Ver casos ocurridos en",
 value=datetime(2020, 1, 1, 9, 30),
 format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)
