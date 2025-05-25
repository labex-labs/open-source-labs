# Gerar Dados e Plotar um Histograma Simples

Para gerar um histograma 1D, precisamos apenas de um único vetor de números. Para um histograma 2D, precisaremos de um segundo vetor. Geraremos ambos abaixo e mostraremos o histograma para cada vetor.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# Generate two normal distributions
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
