# Определим функцию для получения начальных средних значений

Далее мы определим функцию `get_initial_means`, которая принимает на вход выборочные данные, метод инициализации и случайное состояние и возвращает начальные средние значения.

```python
def get_initial_means(X, init_params, r):
    # Run a GaussianMixture with max_iter=0 to output the initialization means
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
