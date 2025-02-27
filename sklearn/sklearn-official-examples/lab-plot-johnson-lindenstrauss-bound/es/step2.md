# Límites teóricos (continuación)

La segunda gráfica muestra que un aumento de la distorsión admisible `eps` nos permite reducir el número mínimo de dimensiones `n_components` para un número dado de muestras `n_samples`.

```python
# rango de distorsiones admisibles
eps_range = np.linspace(0.01, 0.99, 100)

# rango de número de muestras (observaciones) a incrustar
n_samples_range = np.logspace(2, 6, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, color in zip(n_samples_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, color=color)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="upper right")
plt.xlabel("Distorsión eps")
plt.ylabel("Número mínimo de dimensiones")
plt.title("Límites de Johnson-Lindenstrauss:\nn_components vs eps")
plt.show()
```
