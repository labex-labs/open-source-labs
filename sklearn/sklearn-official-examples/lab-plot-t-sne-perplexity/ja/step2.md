# データの作成

t-SNE の使用方法を示すために、3 つの異なるデータセットを作成します。最初のデータセットは、2 つの同心円です。

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```
