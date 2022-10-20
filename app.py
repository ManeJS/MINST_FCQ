import streamlit as st
st.title("Mi aplicación")
st.sidebar.header("Esta aplicación es solo un demo")
st.sidebar.image("http://fcq.uach.mx/index.php/institucionales2-0/columna-2/escudos-institucionales/")
boton = st.button("globos")
if boton:
  st.balloon()
