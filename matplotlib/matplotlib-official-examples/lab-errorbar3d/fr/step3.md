# Générer les données pour le tracé

Nous générons les données pour notre tracé en créant une courbe paramétrique. Une courbe paramétrique est un ensemble d'équations qui décrivent les coordonnées x, y et z en fonction d'un paramètre. Nous utilisons la fonction `arange` de NumPy pour créer un tableau de valeurs allant de 0 à 2π. Nous utilisons ensuite ces valeurs pour calculer les coordonnées x, y et z en utilisant des fonctions trigonométriques.

```python
t = np.arange(0, 2*np.pi+.1, 0.01)
x, y, z = np.sin(t), np.cos(3*t), np.sin(5*t)
```
