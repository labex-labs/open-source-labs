# プロット用のメッシュ作成

次に、プロット用のメッシュを作成します。このメッシュは、メッシュ上の各点に対する予測確率をプロットするために使用されます。また、メッシュの刻み幅も定義します。

```python
h = 0.02  # メッシュの刻み幅

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
