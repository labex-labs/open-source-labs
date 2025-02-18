# Création d'un diagramme à barres avec une valeur alpha explicite

Dans cette étape, nous allons créer un diagramme à barres en utilisant la méthode `bar` de Matplotlib. Nous allons définir la valeur alpha en utilisant l'argument mot-clé `alpha`. Toutes les barres du diagramme auront la même valeur alpha.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)
ax.set_title("Explicit 'alpha' keyword value\nshared by all bars and edges")

plt.show()
```
