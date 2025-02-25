# Définition de la fonction de mouvement aléatoire

Nous définissons une fonction qui génère un mouvement aléatoire avec un nombre donné de pas et une taille maximale de pas. La fonction prend deux entrées : `num_steps` est le nombre total de pas dans le mouvement aléatoire et `max_step` est la taille maximale de chaque pas. Nous utilisons `numpy.random` pour générer des nombres aléatoires pour les pas et `numpy.cumsum` pour calculer la somme cumulative des pas pour obtenir la position finale.

```python
def random_walk(num_steps, max_step=0.05):
    """Retourne un mouvement aléatoire en 3D sous forme d'un tableau (num_steps, 3)."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
