import streamlit as st 

import pandas as pd 

import numpy as np

from datetime import time


st.title('UPC Data Science 2024')

st.header('Simulador Ventas')

n = st.slider("cant. ventas", 5,100, step=1)

chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])

st.line_chart(chart_data)




appointment = st.slider(
 "Programe la asesoria:",
 value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)
