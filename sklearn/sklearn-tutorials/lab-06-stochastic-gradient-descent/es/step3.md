# Preprocesar datos

Antes de aplicar el SGD, a menudo es beneficioso preprocesar los datos. En este caso, estandarizaremos las características utilizando StandardScaler de scikit-learn.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
