# 设置刻度标签

默认情况下，负值处的刻度标签使用 Unicode 减号而非 ASCII 连字符来呈现。不过，我们可以通过将 `axes.unicode_minus` 设置为 `False` 来改变这种行为。

```python
plt.rcParams['axes.unicode_minus'] = False
```
