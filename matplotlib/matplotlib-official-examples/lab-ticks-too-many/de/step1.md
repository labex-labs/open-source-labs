# Überprüfen des Datentyps

Der erste Schritt besteht darin, den Datentyp der x-Achsenwerte zu überprüfen. Wenn es sich um eine Liste von Zeichenketten handelt, ist es wahrscheinlich, dass das Tick-Verhalten unerwartet ist. Um dies zu beheben, müssen wir die Zeichenketten in numerische Typen umwandeln. Hier ist ein Beispiel:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Categories')
plt.show()
```

In diesem Beispiel haben wir eine Liste von Zeichenketten auf der x-Achse. Wenn wir die Daten darstellen, sind die Tick-Labels nicht in der richtigen Reihenfolge und an der falschen Stelle.
