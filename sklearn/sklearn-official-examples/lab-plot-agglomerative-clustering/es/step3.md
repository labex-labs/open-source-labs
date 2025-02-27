# Crear un gráfico

Crea un gráfico que captura la conectividad local. Un mayor número de vecinos dará clústeres más homogéneos a costa del tiempo de cálculo. Un número muy grande de vecinos da tamaños de clúster más uniformemente distribuidos pero puede no imponer la estructura local de la variedad de los datos.

```python
knn_graph = kneighbors_graph(X, 30, include_self=False)
```
