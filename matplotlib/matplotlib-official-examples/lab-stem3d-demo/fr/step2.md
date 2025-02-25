# Définissez les données

Dans cette étape, nous allons définir les données que nous utiliserons pour créer le graphique en batonnet 3D. Nous allons créer un tableau `linspace` pour l'angle, et utiliser les fonctions sinus et cosinus pour calculer les coordonnées x et y. Nous définirons également la coordonnée z comme étant l'angle.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
