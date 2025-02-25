# Das Verständnis der Auswirkungen von doppelten Labels

Doppelte Labels können das Verhalten bestimmter Operationen in pandas verändern. Beispielsweise funktionieren einige Methoden nicht, wenn Duplikate vorhanden sind.

```python
# Creating a pandas Series with duplicate labels
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Attempting to reindex the Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
