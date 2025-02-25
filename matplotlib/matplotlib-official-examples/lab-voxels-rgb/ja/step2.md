# 座標と色の定義

次に、プロット用の座標と色を定義する必要があります。この例では、RGB色の値の17x17x17のグリッドを作成するために、`np.indices`関数を使用します。

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

また、グリッド内の値の間の中点を見つけるための`midpoints`関数も定義します。これは後で球体を作成するために使用されます。

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
