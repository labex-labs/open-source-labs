# Criar e Ajustar o Classificador

Criamos uma instância do classificador Nearest Centroid com um valor de encolhimento de 0,2 e ajustamos os dados.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```
