# Création de données

Nous allons créer certaines données qui seront utilisées pour illustrer le concept de rastérisation.

```python
d = np.arange(100).reshape(10, 10)  # les valeurs à mapper en couleur
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  # faire tourner x de -theta
yy = x*np.sin(theta) + y*np.cos(theta)  # faire tourner y de -theta
```
