# Indizierung mit NA-Werten

Pandas ermöglicht die Indizierung mit `NA`-Werten in einem booleschen Array, die als `False` behandelt werden.

```python
# Erstellen einer pandas-Serie
s = pd.Series([1, 2, 3])

# Erstellen eines booleschen Arrays mit NA-Werten
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indizieren der Serie mit dem booleschen Array
s[mask] # NA-Werte werden als False behandelt
```

Wenn Sie die `NA`-Werte beibehalten möchten, können Sie sie manuell mit `fillna(True)` auffüllen.

```python
# Auffüllen von NA-Werten mit True und Indizieren der Serie
s[mask.fillna(True)]
```
