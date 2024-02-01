import pandas as pd
import seaborn as sns

# Criando dataframe a partir do arquivo csv
gasolina_df = pd.read_csv('./gasolina.csv', sep=',')

# Gerando o gráfico
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço médio da gasolina na cidade de São Paulo nos primeiros dias de Julho de 2021', xlabel='Dias', ylabel='Preço Médio (R$)')

# Salvando o gráfico em uma imagem
grafico.get_figure().savefig('./gasolina.png')
