# Gerar Dados

Neste passo, geramos dados utilizando a função `numpy.random.RandomState` e os parâmetros definidos no Passo 3.

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```
