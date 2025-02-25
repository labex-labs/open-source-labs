# Umgang mit Datum/Uhrzeit-Tick-Marks

Wenn Sie mit Datum/Uhrzeit-Werten auf der x-Achse arbeiten, ist es wichtig, die Zeichenketten in Datetime-Objekte umzuwandeln, um die richtigen Datums-Lokalisierer und -Formatter zu erhalten. Hier ist ein Beispiel:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with datetime strings
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convert strings to datetime64
x = np.asarray(x, dtype='datetime64[s]')

# plot the data with datetime tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

In diesem Beispiel wandeln wir die Zeichenkettwerte in datetime64 um, indem wir `np.asarray()` verwenden. Wenn wir die Daten erneut darstellen, sind die Tick-Labels wie erwartet.
