import streamlit as st
# streamlit é bom para pop (prova de conceito) e tambem para minimo produto viavel, no entanto noa é indicado para projetos robustos

from functions.plotly_ts import plot

st.title("Histórico de cotações")

st.write("veja o histórico das cotações das empresas")

ticker = st.sidebar.text_input('escolha o ticker:', value = 'AAPL')

fig = plot(ticker)

# em pyton podesmos usar fstring, nao entendi muito bem oq é, msas funciona colocando um f antes da string (pesquisar)