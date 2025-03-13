import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("This is my streamlit for 13 March")
st.heading("This module code is EDAB6808")
st.subheading("This is a fun and interactive module")

# Generate random time series data
time_series = np.random.randn(100)


variable = st.button("This is my button")
if variable: 
  time_series = np.random.randn(2000)
  fig,ax = plt.subplots()
  ax.plot(time_series)
  ax.set_title("This is my graph title")
  ax.set_xlabel("Units")
  ax.set_ylabel("Value")
  st.pyplot(fig)
  
# Plot the time series
plt.plot(time_series)
plt.title("Random 100-Unit Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
