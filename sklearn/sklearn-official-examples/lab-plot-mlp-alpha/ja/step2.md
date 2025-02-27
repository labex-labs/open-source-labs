# アルファの定義

正則化パラメータであるalphaの異なる値を定義します。0.1と10の間で対数的に等間隔な5つの値を生成するためにnp.logspaceを使用します。

```python
alphas = np.logspace(-1, 1, 5)
```
