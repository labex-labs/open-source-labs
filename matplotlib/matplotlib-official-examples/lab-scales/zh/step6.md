# 创建自定义比例图

我们要探索的最后一种比例变换类型是自定义比例。这使我们能够为比例变换定义自己的正向和反向函数。在这个例子中，我们将定义一个自定义函数来对数据取平方根。要创建自定义比例图，我们使用 `set_yscale()` 方法并传入字符串 `'function'`。我们还定义 `forward()` 和 `inverse()` 函数，并将它们作为参数传递给 `functions` 参数。我们同样会给图添加标题和网格。

```python
# Function x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
