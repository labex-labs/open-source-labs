# Обучение модели

Мы будем использовать модель GPC для классификации данных. Сначала нужно указать функцию ядра.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Затем можно создать модель GPC и обучить ее с использованием данных.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
