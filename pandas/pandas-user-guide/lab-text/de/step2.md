# String-Methoden verwenden

Pandas bietet eine Reihe von String-Verarbeitungs-Methoden, die es ermöglichen, mit String-Daten einfach umzugehen. Diese Methoden schließen automatisch fehlende/NA-Werte aus.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# in Kleinbuchstaben umwandeln
s.str.lower()

# in Großbuchstaben umwandeln
s.str.upper()

# berechne die Länge jedes Strings
s.str.len()
```
