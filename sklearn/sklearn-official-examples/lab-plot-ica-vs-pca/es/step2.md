# Utilizar el algoritmo PCA

En este paso, utilizamos el algoritmo PCA para encontrar direcciones ortogonales en el espacio de características bruto que corresponden a las direcciones que representan la varianza máxima.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
