# Erstellen eines Streudiagramms auf einer polaren Achse

Wir werden mit der Funktion `plt.scatter()` ein Streudiagramm auf einer polaren Achse erstellen. Wir werden den Parameter `projection` auf `'polar'` setzen und die Radius-, Winkel-, Farb- und Flächenwerte als Parameter übergeben.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
