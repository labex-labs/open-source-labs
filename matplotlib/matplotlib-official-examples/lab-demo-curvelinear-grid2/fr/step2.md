# Définition des fonctions de transformation

La deuxième étape consiste à définir les fonctions de transformation. Dans cet exemple, nous utiliserons la fonction `tr` pour transformer les valeurs de l'axe des x et laisser les valeurs de l'axe des y inchangées. La fonction `inv_tr` sera utilisée pour inverser la transformation.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
