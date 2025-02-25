# Dataframes erstellen

Wir können einen `DataFrame` erstellen, indem wir ein Numpy-Array übergeben, mit einem Zeitstempel-Index und markierten Spalten.

```python
# Creating a pandas dataframe
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
