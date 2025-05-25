# PLSRegression

#### Ajustar o modelo PLSRegression

Começaremos com o algoritmo `PLSRegression`, que é uma forma de regressão linear regularizada. Ajustaremos o modelo aos nossos dados.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Transformar os dados

Podemos transformar os dados originais usando o modelo ajustado. Os dados transformados terão dimensões reduzidas.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
