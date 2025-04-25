# データの生成

次に、ヒストグラムに使用するためのランダムな 2 次元データを生成します。x と y の両方の変数について、NumPy の `random.rand()` 関数を使用して 100 個のランダムな値を生成します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
