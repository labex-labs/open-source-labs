# Création de la grille

Ensuite, nous allons créer la grille dans les coordonnées polaires et calculer la Z correspondante. Nous allons créer un tableau de valeurs de rayon `r`, un tableau de valeurs d'angle `p`, puis utiliser la fonction `meshgrid()` de NumPy pour créer une grille de valeurs de `R` et `P`. Enfin, nous utiliserons l'équation `Z` pour calculer la hauteur de chaque point sur la surface.

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```
