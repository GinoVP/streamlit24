import streamlit as st 

import pandas as pd 

import numpy as np

import datetime

#Ingresando Titulo
st.title('UPC Data Science 2024')

#Creando linea de tiempo
st.header('Simulador Ventas')
n = st.slider("cant. ventas", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])
st.line_chart(chart_data)


start_time = st.slider(
 "Ver casos ocurridos en",
 value=datetime(2020, 1, 1, 9, 30),
 format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)
