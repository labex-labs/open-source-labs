# Création d'un diagramme à barres avec des valeurs alpha variables

Dans cette étape, nous allons créer un diagramme à barres en utilisant la méthode `bar` de Matplotlib. Nous allons définir la valeur alpha en utilisant le format de couleur `(matplotlib_color, alpha)`. Chaque barre du diagramme aura une valeur alpha différente, en fonction de sa valeur y.

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

# Normalize y values to get distinct face alpha values.
abs_y = [abs(y) for y in y_values]
face_alphas = [n / max(abs_y) for n in abs_y]
edge_alphas = [1 - alpha for alpha in face_alphas]

colors_with_alphas = list(zip(facecolors, face_alphas))
edgecolors_with_alphas = list(zip(edgecolors, edge_alphas))

ax.bar(x_values, y_values, color=colors_with_alphas,
        edgecolor=edgecolors_with_alphas)
ax.set_title('Normalized alphas for\neach bar and each edge')

plt.show()
```
