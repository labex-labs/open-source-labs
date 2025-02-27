# サンプルをプロットする

`matplotlib.pyplot` の `scatter` 関数を使って、サンプルをプロットします。

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```
