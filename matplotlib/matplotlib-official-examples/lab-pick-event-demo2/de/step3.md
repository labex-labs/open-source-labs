# Die Daten plotten

Jetzt werden wir mu gegen sigma mit dem pyplot-Modul von Matplotlib plotten. Wir werden einen Punktwolkenplot mit den berechneten Werten für mu und sigma erstellen. Wir fügen auch Interaktivität zum Plot hinzu, indem wir den `picker`-Parameter auf True setzen.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
