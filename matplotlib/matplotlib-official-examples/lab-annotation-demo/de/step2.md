# Verwendung mehrerer Koordinatensysteme und Achsenarten

Sie können die `xypoint` und das `xytext` an verschiedenen Positionen und in verschiedenen Koordinatensystemen angeben und optional eine verbindende Linie aktivieren und den Punkt mit einem Marker markieren. Annotations funktionieren auch auf polaren Achsen.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(3, 3))
r = np.arange(0, 1, 0.001)
theta = 2*2*np.pi*r
line, = ax.plot(theta, r)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom')
```
