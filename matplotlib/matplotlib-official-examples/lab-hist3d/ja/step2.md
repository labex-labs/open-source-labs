# データの生成

次に、ヒストグラムに使用するためのランダムな2次元データを生成します。xとyの両方の変数について、NumPyの `random.rand()` 関数を使用して100個のランダムな値を生成します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
