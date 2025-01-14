import yfinance as yf
import pandas as pd
import fundamentus as fu



carteira_yf = ['ABEV3.SA', 'B3SA3.SA', 'ELET3.SA', 'GGBR4.SA', 'ITSA4.SA',
               'PETR4.SA', 'RENT3.SA', 'SUZB3.SA', 'VALE3.SA', 'WEGE3.SA']

df = yf.download(carteira_yf, start="2022-08-01", end="2023-08-01")

dfAtivo = df.stack(level=1, future_stack=True)

dfAtivo = dfAtivo.reset_index().rename(columns={"Ticker": "Ativo"})

dfAtivo = dfAtivo[["Date", "Open", "Low", "High", "Close", "Ativo"]]

We=fu.get_papel('WEGE3')

carteiraFu = ["ABEV3", "B3SA3", "ELET3", "GGBR4", "ITSA4", 
              "PETR4", "RENT3", "SUZB3", "VALE3", "WEGE3"]

# Obter os dados do Fundamentus para cada papel da carteira
ind = pd.concat([fu.get_papel(papel)[['Setor', 'Cotacao', 'Min_52_sem', 'Max_52_sem', 'Valor_de_mercado', 'Nro_Acoes', 
                                      'Patrim_Liq','Receita_Liquida_12m','Receita_Liquida_3m', 
                                      'Lucro_Liquido_12m', 'Lucro_Liquido_3m']] for papel in carteiraFu])

# Resetar os índices e renomear a coluna 'Ticker' para 'Ativo'
ind = ind.reset_index()
ind.rename(columns={"Ticker": "Ativo"}, inplace=True)
# Definir as colunas a serem convertidas para valores numéricos
colunas = ['Cotacao', 'Min_52_sem', 'Max_52_sem', 'Valor_de_mercado', 'Nro_Acoes', 'Patrim_Liq',
           'Receita_Liquida_12m', 'Receita_Liquida_3m', 'Lucro_Liquido_12m', 'Lucro_Liquido_3m']

# Converter as colunas para valores numéricos, tratando erros
ind[colunas] = ind[colunas].apply(pd.to_numeric, errors='coerce', axis=1)

# Exibir apenas as colunas desejadas
print(ind[['Ativo'] + colunas].head(3))

# Limpar variáveis não utilizadas
del carteiraFu, ind



