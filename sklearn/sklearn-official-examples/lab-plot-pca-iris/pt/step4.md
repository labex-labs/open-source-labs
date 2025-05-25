# Executar PCA

Agora que visualizamos o conjunto de dados, vamos executar a PCA nele. Usaremos a função `PCA()` do scikit-learn para isso. Definiremos o número de componentes para 3, pois queremos reduzir o conjunto de dados de 4 dimensões (4 características) para 3 dimensões.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
