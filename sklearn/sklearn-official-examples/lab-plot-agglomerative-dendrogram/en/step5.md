# Plot the dendrogram

We will plot the dendrogram using the `dendrogram()` function from the `scipy.cluster.hierarchy` module and the `plot_dendrogram()` function defined in the original code.

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
