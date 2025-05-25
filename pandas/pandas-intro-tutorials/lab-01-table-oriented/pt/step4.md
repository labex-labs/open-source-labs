# Realizando Estatísticas Básicas

Pandas oferece muitas funcionalidades para realizar estatísticas. Por exemplo, você pode encontrar o valor máximo em uma coluna usando `max()`.

```python
# Finding the maximum age
df["Age"].max()
```

Você também pode obter uma visão geral rápida dos dados numéricos em um DataFrame usando `describe()`.

```python
# Describing the numerical data
df.describe()
```
