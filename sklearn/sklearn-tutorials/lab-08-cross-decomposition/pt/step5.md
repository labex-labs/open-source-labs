# CCA

#### Ajustar o modelo CCA

O algoritmo `CCA` é um caso especial de PLS e representa a Análise de Correlação Canônica. Ele encontra a correlação entre dois conjuntos de variáveis.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### Transformar os dados

Podemos transformar os dados originais usando o modelo ajustado. Os dados transformados terão dimensões reduzidas.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
