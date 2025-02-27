# Agrupar los datos

Una vez que se ha ajustado el modelo, podemos utilizarlo para agrupar los datos asignando cada muestra al componente gaussiano al que pertenece. El método `predict` de la clase `GaussianMixture` se puede utilizar para este propósito.

```python
# Agrupar los datos
cluster_labels = gmm.predict(X_test)
```
