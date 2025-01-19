import yfinance as yf
import pandas as pd
import fundamentus as fu
from io import StringIO
from cotacoes import Cotacoes
from indicadores import Indicadores
class Main:
    def __init__(self):
        self.cotacoes = Cotacoes()
        self.indicadores = Indicadores()

    def executar(self):
       
        print("Calculando indicadores principais (ind)...")
        ind = self.indicadores.indicadores()

        print("\nCalculando indicadores adicionais (ind_2)...")
        ind_2 = self.indicadores.indicadores2()

        if ind is not None and ind_2 is not None:
            print("\nMesclando indicadores (ind + ind_2)...")
            indicadores_completos = self.indicadores.mesclagem(ind, ind_2)
            print(indicadores_completos)
        else:
            print("\nErro: Não foi possível calcular os indicadores.")

if __name__ == "__main__":
    programa = Main()
    programa.executar()