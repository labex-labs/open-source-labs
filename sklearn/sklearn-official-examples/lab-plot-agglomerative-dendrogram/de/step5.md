# Dendrogramm zeichnen

Wir werden das Dendrogramm mit der `dendrogram()` - Funktion aus dem `scipy.cluster.hierarchy` - Modul und der in dem ursprünglichen Code definierten `plot_dendrogram()` - Funktion zeichnen.

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
