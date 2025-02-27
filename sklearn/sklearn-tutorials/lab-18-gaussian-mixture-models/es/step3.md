# Ajustar un Modelo Mixto Gaussiano

Ahora, podemos ajustar un Modelo Mixto Gaussiano a nuestros datos utilizando la clase `GaussianMixture` del módulo `sklearn.mixture`. Especifique el número deseado de componentes y cualquier otro parámetro que desee utilizar.

```python
# Ajustar un Modelo Mixto Gaussiano
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
