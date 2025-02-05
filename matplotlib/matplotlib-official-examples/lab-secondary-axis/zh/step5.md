# 创建次 x 轴

我们将创建次 x 轴，并将频率转换为周期。我们将使用 `one_over` 作为正向函数，`inverse` 作为反向函数。

```python
def one_over(x):
    """向量化的 1/x，手动处理 x==0 的情况"""
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x

# 函数“1/x”自身即为其反函数
inverse = one_over

secax = ax.secondary_xaxis('top', functions=(one_over, inverse))
secax.set_xlabel('period [s]')
```
