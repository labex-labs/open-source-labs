# Wertumsetzung

Das Umsetzen eines Werts **überschreibt niemals** den von dem vorherigen Wert verwendeten Arbeitsspeicher.

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]    Behält den ursprünglichen Wert bei
```

Denken Sie daran: **Variablen sind Namen, nicht Arbeitsspeicheradressen.**
