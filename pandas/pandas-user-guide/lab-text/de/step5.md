# Dummy-Variablen erstellen

Sie können Dummy-Variablen aus String-Daten mit der `get_dummies`-Methode erstellen.

```python
# erstelle Dummy-Variablen
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
