# Erstellen eines Streudiagramms auf einer polaren Achse mit versetztem Ursprung

Wir können ein Streudiagramm auf einer polaren Achse mit einem versetzten Ursprung erstellen, indem wir die Methoden `set_rorigin()` und `set_theta_zero_location()` des `PolarAxes`-Objekts festlegen. Wir werden den Ursprungsradius auf `-2,5` und die Theta-Null-Lage auf `'W'` mit einem Offset von `10` setzen.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
