# Créer un noyau personnalisé

Dans cette étape, nous allons créer un noyau personnalisé. Le noyau personnalisé sera un produit scalaire de deux matrices. Nous allons créer une matrice M avec les valeurs [[2, 0], [0, 1,0]]. Nous multiplierons ensuite les matrices X et Y par M et prendrons leur produit scalaire.

```python
def my_kernel(X, Y):
    """
    Nous créons un noyau personnalisé :

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)
```
