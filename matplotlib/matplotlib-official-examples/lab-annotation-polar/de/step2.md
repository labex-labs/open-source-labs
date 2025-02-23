# Erstellen eines Polarkoordinaten-Graphen

Als nächstes erstellen wir einen Polarkoordinaten-Graphen, indem wir die Figur definieren und angeben, dass sie eine Polarkoordinatenprojektion hat. Wir definieren auch den Radius und die Theta-Werte, die bei der Darstellung verwendet werden sollen.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```
