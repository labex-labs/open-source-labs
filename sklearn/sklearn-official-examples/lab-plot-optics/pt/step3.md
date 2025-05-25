# Executar o Algoritmo de Agrupamento OPTICS

Agora, executaremos o algoritmo de agrupamento OPTICS nos dados gerados. Neste exemplo, definimos `min_samples=50`, `xi=0.05` e `min_cluster_size=0.05`.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
