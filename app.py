import streamlit as st
from functions.plotly_ts import plot

st.title('Historico de cotação')

st.write('Veja o historico das transações')

ticker = st.sidebar.text_input('Escolha o ticker:',  value = 'AAPL')

fig = plot(ticker)

st.plotly_chart(fig)
st.image("imagens/frame.png")

# em pyton podesmos usar fstring, nao entendi muito bem oq é, msas funciona colocando um f antes da string (pesquisar)
# streamlit é bom para pop (prova de conceito) e tambem para minimo produto viavel, no entanto noa é indicado para projetos robustos