# CCA

#### Ajustar el modelo de CCA

El algoritmo `CCA` es un caso especial de PLS y significa Análisis de Correlación Canónica. Encuentra la correlación entre dos conjuntos de variables.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### Transformar los datos

Podemos transformar los datos originales utilizando el modelo ajustado. Los datos transformados tendrán una dimensión reducida.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
