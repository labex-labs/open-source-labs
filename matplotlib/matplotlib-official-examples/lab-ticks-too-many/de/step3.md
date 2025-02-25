# Umgang mit zu vielen Tick-Marks

Wenn die x-Achse viele Elemente hat, von denen alle Zeichenketten sind, können wir zu viele unlesbare Tick-Marks erhalten. In diesem Fall müssen wir die Zeichenketten in numerische Typen umwandeln. Hier ist ein Beispiel:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Categories')
plt.show()
```

In diesem Beispiel haben wir 100 Zeichenkettwerte auf der x-Achse, was zu vielen unlesbaren Tick-Marks führt.

Um dies zu beheben, müssen wir die Zeichenketten in Floats umwandeln. Hier ist ein Beispiel:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# convert strings to floats
x = np.asarray(x, float)

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Floats')
plt.show()
```

In diesem Beispiel wandeln wir die Zeichenkettwerte in Floats um, indem wir `np.asarray()` verwenden. Wenn wir die Daten erneut darstellen, sind die Tick-Labels wie erwartet.
