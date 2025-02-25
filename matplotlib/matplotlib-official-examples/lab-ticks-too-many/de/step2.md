# Umwandeln von Zeichenketten in numerische Typen

Um das Tick-Verhalten zu beheben, müssen wir die Zeichenketten in numerische Typen umwandeln. Hier ist ein Beispiel:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convert strings to floats
x = np.asarray(x, dtype='float')

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

In diesem Beispiel wandeln wir die Zeichenkettwerte in Floats um, indem wir `np.asarray()` verwenden. Wenn wir die Daten erneut darstellen, sind die Tick-Labels wie erwartet.
