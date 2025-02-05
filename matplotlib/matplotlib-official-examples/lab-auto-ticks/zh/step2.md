# 采用 round_numbers 自动限制模式的散点图

在这一步中，我们将把 `axes.autolimit_mode` 切换为 'round_numbers'，并创建一个散点图，使刻度保持为整数，同时在边缘也有刻度。

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
