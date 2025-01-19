import yfinance as yf
import pandas as pd
import fundamentus as fu
from io import StringIO


class Cotacoes:

    def __init__(self):
        self.carteira_yf = ['ABEV3.SA', 'B3SA3.SA', 'ELET3.SA', 'GGBR4.SA', 'ITSA4.SA',
               'PETR4.SA', 'RENT3.SA', 'SUZB3.SA', 'VALE3.SA', 'WEGE3.SA']
  
    def obter_cotacoes(self):
      df = yf.download(carteira_yf, start="2022-08-01", end="2023-08-01")
      dfAtivo =dfAtivo = df.stack(level=1, future_stack=True).reset_index()
      dfAtivo.rename(columns={"Ticker": "Ativo"}, inplace=True)
      dfAtivo = dfAtivo[["Date", "Open", "Low", "High", "Close", "Ativo"]]
      return cotacoes
