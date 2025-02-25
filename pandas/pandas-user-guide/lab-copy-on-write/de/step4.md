# Implementieren von verketteter Zuweisung mit Copy-On-Write

Schließlich sehen wir uns an, wie man die verkettete Zuweisung mit Copy-On-Write mit der `loc`-Methode implementiert.

```python
# Erstellen eines DataFrames
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Anwenden der verketteten Zuweisung mit Copy-On-Write mit 'loc'
df.loc[df["bar"] > 5, "foo"] = 100

# Ausgabe des DataFrames
print(df)
```
