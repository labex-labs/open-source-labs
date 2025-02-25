# Définir la fonction d'animation

La sixième étape consiste à définir la fonction d'animation. Cette fonction sera appelée pour chaque trame de l'animation et mettra à jour la position du point sur le sous-graphique de gauche, la position et les données de la courbe sinusoidale sur le sous-graphique de droite, et la position du patch de connexion.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
