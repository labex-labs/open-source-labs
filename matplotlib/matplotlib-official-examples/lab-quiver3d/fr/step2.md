# Création de la grille

Ensuite, nous allons créer une grille de points sur laquelle nous allons afficher le champ de vecteurs. Dans cet exemple, nous allons créer une grille de points à l'aide de la fonction `meshgrid` de NumPy. La fonction `arange` est utilisée pour créer un tableau de points régulièrement espacés dans un intervalle spécifié.

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```
