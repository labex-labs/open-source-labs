# PLSSVD

#### Ajustar el modelo de PLSSVD

El algoritmo `PLSSVD` es una versión simplificada de `PLSCanonical` que calcula la Descomposición en Valores Singulares (SVD) de la matriz de covarianza cruzada solo una vez. Este algoritmo es útil cuando el número de componentes está limitado a uno.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### Transformar los datos

Podemos transformar los datos originales utilizando el modelo ajustado. Los datos transformados tendrán una dimensión reducida.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
