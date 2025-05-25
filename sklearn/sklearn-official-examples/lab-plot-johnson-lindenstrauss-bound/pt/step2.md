# Limites Teóricos (continuação)

O segundo gráfico demonstra que um aumento da distorção admissível `eps` permite reduzir o número mínimo de dimensões `n_components` para um determinado número de amostras `n_samples`.

```python
# intervalo de distorções admissíveis
eps_range = np.linspace(0.01, 0.99, 100)

# intervalo do número de amostras (observações) a serem incorporadas
n_samples_range = np.logspace(2, 6, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, color in zip(n_samples_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, color=color)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="upper right")
plt.xlabel("Distorção eps")
plt.ylabel("Número mínimo de dimensões")
plt.title("Limites de Johnson-Lindenstrauss:\nn_components vs eps")
plt.show()
```
