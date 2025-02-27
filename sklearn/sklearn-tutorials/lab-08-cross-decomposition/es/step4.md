# PLSCanonical

#### Ajustar el modelo de PLSCanonical

A continuación, usaremos el algoritmo `PLSCanonical`, que encuentra la correlación canónica entre dos matrices. Este algoritmo es útil cuando hay multicolinealidad entre las características.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### Transformar los datos

Podemos transformar los datos originales utilizando el modelo ajustado. Los datos transformados tendrán una dimensión reducida.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
