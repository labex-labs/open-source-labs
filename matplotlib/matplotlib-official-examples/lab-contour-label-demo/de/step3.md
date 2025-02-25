# Bezeichnen von Konturen mit beliebigen Zeichenketten mithilfe eines Wörterbuchs

Wir können auch Konturen mit beliebigen Zeichenketten mithilfe eines Wörterbuchs bezeichnen. Dies wird uns ermöglichen, die Konturen mit benutzerdefinierten Bezeichnungen zu versehen. In diesem Beispiel werden wir eine Liste von Zeichenketten verwenden, um die Konturen zu bezeichnen.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first','second', 'third', 'fourth', 'fifth','sixth','seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
