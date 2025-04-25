# 创建墨卡托变换比例图

作为额外内容，我们还将使用墨卡托变换函数创建一个图。这不是 Matplotlib 中的内置函数，但我们可以定义自己的正向和反向函数来创建墨卡托变换比例图。在这个例子中，我们将为墨卡托变换定义 `forward()` 和 `inverse()` 函数。我们还会给图添加标题和网格。

```python
# Function Mercator transform
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
