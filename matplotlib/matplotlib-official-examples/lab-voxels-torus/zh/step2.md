# 定义中点函数

接下来，我们定义一个`midpoints`函数来计算坐标数组的中点。该函数稍后将用于计算`r`、`theta`和`z`的中点。

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
