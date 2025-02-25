# Ausführen von Operationen mit nullable Integer-Arrays

Sie können verschiedene Operationen mit nullable Integer-Arrays durchführen, wie arithmetische Operationen, Vergleiche und Slicing.

```python
# Erstellen einer Series mit nullable Integer-Typ
s = pd.Series([1, 2, None], dtype="Int64")

# Ausführen einer arithmetischen Operation
s_plus_one = s + 1 # addiert 1 zu jedem Element in der Series

# Ausführen eines Vergleichs
vergleich = s == 1 # prüft, ob jedes Element in der Series gleich 1 ist

# Ausführen eines Slicing-Operators
geschnitten = s.iloc[1:3] # wählt das zweite und dritte Element in der Series aus
```
