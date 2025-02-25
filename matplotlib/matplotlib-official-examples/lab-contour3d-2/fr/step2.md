# Création des données

Ensuite, nous devons créer les données que nous utiliserons pour générer le tracé de contour. Nous utiliserons la fonction `get_test_data()` du module `mpl_toolkits.mplot3d` pour générer des données d'échantillonnage.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
