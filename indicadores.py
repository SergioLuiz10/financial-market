import yfinance as yf
import pandas as pd
import fundamentus as fu
from io import StringIO


class Indicadores:
    def __init__(self):
        self.carteiraFu = [
            'ABEV3', 'B3SA3', 'ELET3', 'GGBR4', 'ITSA4',
            'PETR4', 'RENT3', 'SUZB3', 'VALE3', 'WEGE3'
        ]

    def indicadores(self):

        try:
            ind = pd.concat([
                fu.get_papel(papel)[[
                    'Setor', 'Cotacao', 'Min_52_sem', 'Max_52_sem', 'Valor_de_mercado',
                    'Nro_Acoes', 'Patrim_Liq', 'Receita_Liquida_12m', 'Receita_Liquida_3m',
                    'Lucro_Liquido_12m', 'Lucro_Liquido_3m'
                ]].assign(Ativo=papel)
                for papel in self.carteiraFu
            ]).reset_index(drop=True)

            colunas = ['Cotacao', 'Min_52_sem', 'Max_52_sem', 'Valor_de_mercado', 'Nro_Acoes',
                       'Patrim_Liq', 'Receita_Liquida_12m', 'Receita_Liquida_3m',
                       'Lucro_Liquido_12m', 'Lucro_Liquido_3m']
            ind[colunas] = ind[colunas].apply(pd.to_numeric, errors='coerce', axis=1)

            return ind
        except Exception as e:
            print(f"Erro ao calcular indicadores principais: {e}")
            return None

    def indicadores2(self):

        try:
            ind_2 = fu.get_resultado_raw().reset_index()
            ind_2 = ind_2.query("papel in @self.carteiraFu")
            ind_2 = ind_2[['papel', 'P/L', 'Div.Yield', 'P/VP', 'ROE']].reset_index(drop=True)
            ind_2.rename(columns={'papel': 'Ativo', 'Div.Yield': 'DY'}, inplace=True)
            return ind_2
        except Exception as e:
            print(f"Erro ao calcular indicadores adicionais: {e}")
            return None

    def mesclagem(self, ind, ind_2):

        try:
            ind["LPA"] = (ind["Lucro_Liquido_12m"] / ind["Nro_Acoes"]).round(2)
            ind["VPA"] = (ind["Patrim_Liq"] / ind["Nro_Acoes"]).round(2)

            indFU = pd.merge(ind, ind_2, on="Ativo")
            return indFU
        except Exception as e:
            print(f"Erro ao mesclar indicadores: {e}")
            return None
