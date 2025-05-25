# Criando Dataframes

Podemos criar um `DataFrame` passando um array numpy, com um índice de data e hora e colunas rotuladas.

```python
# Creating a pandas dataframe
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
