# Carregando os Dados

Usaremos dados de qualidade do ar para este tutorial. Os dados serão carregados de um arquivo CSV em um DataFrame do Pandas.

```python
# Carregando os dados
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
