# 绘制树形图

我们将使用`scipy.cluster.hierarchy`模块中的`dendrogram()`函数以及原始代码中定义的`plot_dendrogram()`函数来绘制树形图。

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
