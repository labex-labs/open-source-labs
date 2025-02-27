# Entrenar el modelo

Utilizaremos un modelo GPC para clasificar los datos. En primer lugar, necesitamos especificar la función del kernel.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Luego, podemos crear un modelo GPC y entrenarlo utilizando los datos.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
