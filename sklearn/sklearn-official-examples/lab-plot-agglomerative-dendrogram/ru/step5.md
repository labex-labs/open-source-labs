# Построение дендрограммы

Мы построим дендрограмму с использованием функции `dendrogram()` из модуля `scipy.cluster.hierarchy` и функции `plot_dendrogram()`, определенной в исходном коде.

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
