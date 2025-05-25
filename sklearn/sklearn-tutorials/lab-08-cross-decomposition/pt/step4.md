# PLSCanonical

#### Ajustar o modelo PLSCanonical

Em seguida, usaremos o algoritmo `PLSCanonical`, que encontra a correlação canônica entre duas matrizes. Este algoritmo é útil quando há multicolinearidade entre as características.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### Transformar os dados

Podemos transformar os dados originais usando o modelo ajustado. Os dados transformados terão dimensões reduzidas.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
