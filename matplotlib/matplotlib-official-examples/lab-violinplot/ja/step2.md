# サンプルデータセットを作成する

numpy ライブラリを使ってサンプルデータセットを作成します。異なる標準偏差を持つ 6 つのデータセットを作成します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```
