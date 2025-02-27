# PLSRegression

#### Ajustar el modelo de PLSRegression

Comenzaremos con el algoritmo `PLSRegression`, que es una forma de regresión lineal regularizada. Ajustaremos el modelo a nuestros datos.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Transformar los datos

Podemos transformar los datos originales utilizando el modelo ajustado. Los datos transformados tendrán una dimensión reducida.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
