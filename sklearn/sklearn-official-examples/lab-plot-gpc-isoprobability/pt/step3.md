# Treinar o Modelo

Usaremos um modelo GPC para classificar os dados. Primeiro, precisamos especificar a função kernel.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Em seguida, podemos criar um modelo GPC e treiná-lo usando os dados.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
