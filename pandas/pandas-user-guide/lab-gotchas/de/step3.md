# Das Mutieren mit Methoden benutzerdefinierter Funktionen (UDF)

Wenn Sie eine Pandas-Methode verwenden, die eine UDF akzeptiert, vermeiden Sie es, das DataFrame innerhalb der UDF zu ändern. Stattdessen erstellen Sie eine Kopie, bevor Sie Änderungen vornehmen.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
