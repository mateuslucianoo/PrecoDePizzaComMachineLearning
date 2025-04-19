import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()
x = df[["diametro"]]  
y = df[["preco"]]   
modelo.fit(x, y)

st.markdown("<h1 style='text-align: center; color: tomato;'>🍕 Preço de Pizza</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #f63366;'>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Informe o tamanho da pizza em cm:</h3>", unsafe_allow_html=True)
diametro = st.number_input("", min_value=1.0, step=1.0, format="%.0f")

if st.button("Calcular Preço"):
    preco_previsto = modelo.predict([[diametro]])[0][0]

    st.markdown(f"""
    <div style='
        background-color: #ffe6e6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        font-size: 20px;
        color: #333333;
        '>
        O valor da pizza com diâmetro de <strong>{int(diametro)} cm</strong> é de <strong>R${preco_previsto:.2f}</strong>.
    </div>
    """, unsafe_allow_html=True)
