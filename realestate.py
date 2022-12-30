import streamlit as st 
import pandas as pd 

main_title = 'Real Estate Process Manager'

st.title(main_title)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df