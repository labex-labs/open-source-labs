# Realizar estadísticas básicas

Pandas ofrece muchas funcionalidades para realizar estadísticas. Por ejemplo, puede encontrar el valor máximo en una columna utilizando `max()`.

```python
# Encontrando la edad máxima
df["Edad"].max()
```

También puede obtener una visión general rápida de los datos numéricos en un DataFrame utilizando `describe()`.

```python
# Describiendo los datos numéricos
df.describe()
```
