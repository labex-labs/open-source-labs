# データポイントをプロットする

Matplotlib の scatter 関数を使って、入力データポイントをプロットします。

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor="k", s=20)
```
