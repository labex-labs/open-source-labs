# 中点関数の定義

次に、座標の配列の中点を計算するための `midpoints` 関数を定義します。この関数は後で `r`、`theta`、および `z` の中点を計算するために使用されます。

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
