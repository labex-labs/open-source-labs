# Das Verständnis von Copy-On-Write mit DataFrame

Jetzt erstellen wir ein DataFrame und sehen, wie Copy-On-Write die Datenmodifikation beeinflusst.

```python
# Erstellen eines DataFrames
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Erstellen eines Teils des DataFrames
subset = df["foo"]

# Ändern des Teils
subset.iloc[0] = 100

# Ausgabe des ursprünglichen DataFrames
print(df)
```

## Implementieren von Copy-On-Write mit DataFrame

Jetzt sehen wir uns an, wie man Copy-On-Write beim Ändern eines DataFrames implementiert.

```python
# Aktivieren von Copy-On-Write
pd.options.mode.copy_on_write = True

# Erstellen eines Teils des DataFrames
subset = df["foo"]

# Ändern des Teils
subset.iloc[0] = 100

# Ausgabe des ursprünglichen DataFrames
print(df)
```
