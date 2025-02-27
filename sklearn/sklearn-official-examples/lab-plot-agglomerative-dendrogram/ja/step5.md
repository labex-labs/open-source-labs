# デンドログラムを描画する

`scipy.cluster.hierarchy` モジュールの `dendrogram()` 関数と、元のコードで定義された `plot_dendrogram()` 関数を使って、デンドログラムを描画します。

```python
plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
```
