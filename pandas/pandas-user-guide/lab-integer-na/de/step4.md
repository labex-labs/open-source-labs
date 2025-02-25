# Umgang mit fehlenden Werten mit pandas.NA

Die `IntegerArray`-Klasse verwendet `pandas.NA` als skalaren fehlenden Wert. Wenn Sie ein einzelnes fehlendes Element slicen, wird `pandas.NA` zurückgegeben.

```python
# Erstellen eines IntegerArrays mit einem fehlenden Wert
a = pd.array([1, None], dtype="Int64")

# Slicen des zweiten Elements, das ein fehlender Wert ist
fehlender_wert = a[1]
# Ausgabe: <NA>
```
