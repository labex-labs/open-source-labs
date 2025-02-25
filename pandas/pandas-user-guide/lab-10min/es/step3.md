# Creando Dataframes

Podemos crear un `DataFrame` pasando una matriz de numpy, con un índice de fecha y hora y columnas etiquetadas.

```python
# Creando un dataframe de pandas
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
