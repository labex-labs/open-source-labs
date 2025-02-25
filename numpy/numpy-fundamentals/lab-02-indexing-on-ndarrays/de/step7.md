# Zuweisen von Werten an indizierte Arrays

Sie können mit Hilfe von Indexierung Werten an bestimmte Elemente oder Elemente einer Teilmenge in einem Array zuweisen. Der zuzuweisende Wert muss in der Form mit dem indizierten Array übereinstimmen.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Ausgabe: [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Ausgabe: [0, 1, 0, 1, 2, 3, 7, 8, 9]
```
