# Définition de la fonction `get_correlated_dataset`

Nous avons également besoin d'une fonction pour générer un ensemble de données bidimensionnelles avec une moyenne, des dimensions et une corrélation spécifiées.

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    Crée un ensemble de données bidimensionnelles aléatoires avec la moyenne bidimensionnelle (mu) et les dimensions (scale) spécifiées.
    La corrélation peut être contrôlée par le paramètre 'dependency', une matrice 2x2.
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # retourne x et y du nouvel ensemble de données corrélé
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```
