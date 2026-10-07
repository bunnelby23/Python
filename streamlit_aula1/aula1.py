import streamlit as st
import pandas as pd


st.write("""♡ ∩_∩ \n
  („• ֊ •„)♡\n
|￣U U￣￣￣￣￣￣￣￣￣|\n
|            Olá mundo       |   \n
￣￣￣￣￣￣￣￣￣￣￣￣""")

nome = "Coelho"
idade = "17"

st.write("Olá ",nome, "! Se estou correto, sua idade é ",idade, " anos")

# df = pd.DataFrame({
#    'first column': ["Português", "Matemática", "Python", "Frame"],
#    'second column': [5, 9, 7, 10] 
#     })

st.title("Meu primeiro dash")
st.subheader("Coelho")

df = pd.DataFrame({
   'first column': ["Português", "Matemática", "Python", "Frame"],
   'second column': [5, 9, 7, 10] 
    })

df