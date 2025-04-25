# ランダムな行列を作成する

次に、numpy を使ってランダムな行列を作成します。0 から 1 の間のランダムな値を持つ 5x3 の行列を作成するために、`rand` メソッドを使います。また、結果の再現性を保証するために、ランダムシードを設定します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
