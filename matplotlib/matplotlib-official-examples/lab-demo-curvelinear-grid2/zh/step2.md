# 定义变换函数

第二步是定义变换函数。在这个例子中，我们将使用 `tr` 函数来变换 x 轴的值，而 y 轴的值保持不变。`inv_tr` 函数将用于反转该变换。

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
