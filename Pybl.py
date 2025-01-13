import yfinance as yf
import pandas as pd

carteira_yf = ['ABEV3.SA', 'B3SA3.SA', 'ELET3.SA', 'GGBR4.SA', 'ITSA4.SA',
               'PETR4.SA', 'RENT3.SA', 'SUZB3.SA', 'VALE3.SA', 'WEGE3.SA']

df = yf.download(carteira_yf, start="2022-08-01", end="2023-08-01")

dfAtivo = df.stack(level = 1)

dfAtivo=dfAtivo.reset_index().rename(columns={"Ticker": "Ativo"})

dfAtivo = dfAtivo[["Date", "Open", "Low", "High", "Close","Ativo"]]

dfAtivo.info()

del carteira_yf, df


