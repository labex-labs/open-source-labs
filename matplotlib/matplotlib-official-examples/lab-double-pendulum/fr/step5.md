# Calculer la position de chaque pendule

Nous allons maintenant utiliser la position et la vitesse de chaque pendule à chaque pas de temps pour calculer les coordonnées x et y de chaque pendule.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```
