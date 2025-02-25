# Création des données pour le tracé de surface

Dans cette étape, nous allons créer les données pour le tracé de surface. Nous allons créer une grille de maillage de valeurs X et Y, calculer la distance radiale R et calculer la valeur Z en fonction de la valeur de R en utilisant `np.sin()`.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
