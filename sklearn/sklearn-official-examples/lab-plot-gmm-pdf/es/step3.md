# Ajustar el modelo de mezcla gaussiana

Ahora ajustaremos un GMM al conjunto de datos usando la clase GaussianMixture de scikit-learn. Estableceremos el número de componentes en 2 y el tipo de covarianza en "full".

```python
# ajustar un modelo de mezcla gaussiana con dos componentes
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
