# Tracez le dendrogramme

Nous allons tracer le dendrogramme à l'aide de la fonction `dendrogram()` du module `scipy.cluster.hierarchy` et de la fonction `plot_dendrogram()` définie dans le code original.

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
