# Création de DataFrames

Nous pouvons créer un `DataFrame` en passant un tableau numpy, avec un index de dates et des colonnes étiquetées.

```python
# Creating a pandas dataframe
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
