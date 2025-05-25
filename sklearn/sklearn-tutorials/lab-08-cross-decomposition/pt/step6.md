# PLSSVD

#### Ajustar o modelo PLSSVD

O algoritmo `PLSSVD` é uma versão simplificada do `PLSCanonical` que calcula a Decomposição em Valores Singulares (SVD) da matriz de covariância cruzada apenas uma vez. Este algoritmo é útil quando o número de componentes é limitado a um.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### Transformar os dados

Podemos transformar os dados originais usando o modelo ajustado. Os dados transformados terão dimensões reduzidas.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
