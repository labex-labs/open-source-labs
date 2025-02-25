# Création du cercle

Nous allons créer le cercle en utilisant la fonction `make_circle()`. Cette fonction prend le rayon du cercle en entrée et renvoie les coordonnées x et y du cercle.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
