import streamlit as st 

import pandas as pd 

import numpy as np

from datetime import datetime

import datetime as dt

#Ingresando Titulo
st.title('UPC Data Science 2024')

#Creando linea de tiempo
st.header('Simulador Ventas')
n = st.slider("cant. ventas", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])
st.line_chart(chart_data)

#Creando Slider de fecha
start_time = st.slider(
 "Ver casos ocurridos en",
 value=datetime(2020, 1, 1, 9, 30),
 format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)

#Creando Calendario
d = st.date_input(
 "Fecha de cumpleaños",
 dt.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)
