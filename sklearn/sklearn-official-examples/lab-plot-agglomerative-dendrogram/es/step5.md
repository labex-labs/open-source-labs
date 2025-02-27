# Graficar el dendrograma

Graficaremos el dendrograma utilizando la función `dendrogram()` del módulo `scipy.cluster.hierarchy` y la función `plot_dendrogram()` definida en el código original.

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
