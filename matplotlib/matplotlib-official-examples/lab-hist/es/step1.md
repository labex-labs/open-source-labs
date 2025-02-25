# Generar datos y trazar un histograma simple

Para generar un histograma unidimensional, solo necesitamos un solo vector de números. Para un histograma bidimensional, necesitaremos un segundo vector. Generaremos ambos a continuación y mostraremos el histograma para cada vector.

```python
import matplotlib.pyplot as plt
import numpy as np

# Crea un generador de números aleatorios con una semilla fija para la reproducibilidad
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# Genera dos distribuciones normales
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# Podemos establecer el número de bins con el argumento de palabras clave *bins*.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
