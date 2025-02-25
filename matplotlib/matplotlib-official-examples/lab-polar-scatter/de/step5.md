# Erstellen eines Streudiagramms auf einer polaren Achse, das auf einen Sektor beschränkt ist

Wir können ein Streudiagramm auf einer polaren Achse erstellen, das auf einen Sektor beschränkt ist, indem wir die Methoden `set_thetamin()` und `set_thetamax()` des `PolarAxes`-Objekts festlegen. Wir werden die Start- und Endgrenzen von Theta auf `45` und `135` setzen.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
