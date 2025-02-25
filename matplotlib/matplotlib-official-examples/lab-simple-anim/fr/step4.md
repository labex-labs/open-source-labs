# Définir la fonction d'animation

La fonction d'animation sera appelée par la fonction `FuncAnimation()` et servira à mettre à jour le graphique avec de nouvelles données. Dans cet exemple, nous allons mettre à jour les valeurs de l'axe des y du graphique en ligne avec une onde sinusoïdale dont l'amplitude change au fil du temps.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # mettre à jour les données.
    return line,
```
