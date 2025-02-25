# データの作成

0 から 3π の間に等間隔で分布する 500 個の値を含む numpy 配列 `x` を作成します。また、`x` の値のサインを含む別の numpy 配列 `y` も作成します。最後に、`y` の 1 階微分を含む numpy 配列 `dydx` を作成します。

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```
