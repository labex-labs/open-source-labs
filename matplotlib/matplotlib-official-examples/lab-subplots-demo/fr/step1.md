# Création d'une figure avec un seul sous-graphique

La manière la plus simple de créer un seul sous-graphique est d'utiliser la fonction `subplots()` sans aucun argument. Cette fonction renvoie un objet `Figure` et un seul objet `Axes`.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

```
