# Генерируем данные

В этом шаге мы генерируем данные с использованием функции `numpy.random.RandomState` и параметров, определенных на шаге 3.

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
