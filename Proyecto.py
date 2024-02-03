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

#Creando lista de seleccion
option = st.selectbox(
 '¿Cómo desearía ser contactado/a?',
 ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

#Creando un botón para limpiar filtros
if st.button('Limpiar filtros'):
    # Restablecer los valores de los filtros a su estado predeterminado
    start_time = datetime(2020, 1, 1, 9, 30)
    d = dt.date(2019, 7, 6)
    option = 'Email'
