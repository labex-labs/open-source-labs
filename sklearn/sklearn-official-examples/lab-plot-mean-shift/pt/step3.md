# Cálculo de Agrupamento com MeanShift

Agora, calcularemos o agrupamento usando o algoritmo Mean-Shift com a classe `MeanShift` do módulo `sklearn.cluster`. Usaremos a função `estimate_bandwidth` para detectar automaticamente o parâmetro de largura de banda, que representa o tamanho da região de influência para cada ponto.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
