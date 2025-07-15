import pandas as pd 
# ngm usa outro alias que nao seja pd
import matplotlib.pyplot as ptt

tabela = pd.DataFrame({
    'idade':[20, 23, 45, 31, 32],    
    'nomes':['joao', 'maria', 'jose', 'sofia', 'helena']
})

ptt.hist(tabela['idade'])



