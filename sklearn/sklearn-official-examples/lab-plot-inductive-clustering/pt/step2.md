# Treinar o Algoritmo de Agrupamento

Neste passo, treinaremos um algoritmo de agrupamento nos dados de treino gerados e obteremos as etiquetas dos clusters. Usaremos `AgglomerativeClustering` da biblioteca scikit-learn para treinar o algoritmo com 3 clusters.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
