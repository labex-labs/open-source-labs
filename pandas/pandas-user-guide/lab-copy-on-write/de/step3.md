# Das Verständnis von verketteter Zuweisung mit Copy-On-Write

Jetzt verstehen wir, wie die verkettete Zuweisung mit Copy-On-Write funktioniert.

```python
# Erstellen eines DataFrames
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Anwenden der verketteten Zuweisung, die die Copy-On-Write-Prinzipien verletzen würde
df["foo"][df["bar"] > 5] = 100

# Ausgabe des DataFrames
print(df)
```
