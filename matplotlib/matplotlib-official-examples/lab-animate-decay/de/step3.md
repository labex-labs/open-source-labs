# Das Diagramm einrichten

Jetzt müssen wir das Diagramm einrichten. Wir werden eine Figur und ein Achsenobjekt mithilfe der `subplots()`-Funktion von Matplotlib erstellen. Wir werden auch ein Linienobjekt erstellen, um die Sinuswelle darzustellen.

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
