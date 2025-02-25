# Das Diagramm einrichten

Wir richten nun das Diagramm für unsere Simulation ein. Wir erstellen eine Figur mit einer x- und y-Begrenzung, die der maximalen Länge des Pendels entspricht, setzen das Seitenverhältnis gleich und fügen ein Gitter hinzu.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
