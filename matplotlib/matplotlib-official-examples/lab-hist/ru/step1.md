# Генерация данных и построение простой гистограммы

Для построения одномерной гистограммы нам нужен только один вектор чисел. Для двумерной гистограммы потребуется второй вектор. Мы сгенерируем оба ниже и покажем гистограмму для каждого вектора.

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
