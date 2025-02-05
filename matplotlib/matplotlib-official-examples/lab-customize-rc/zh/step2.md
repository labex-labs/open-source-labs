# 自定义默认参数

要为特定图形自定义默认参数，你可以再次使用 `rcParams.update()` 方法。这次，你要传入一个你想为该图形设置的参数名称和值的字典。以下是一个为特定图形设置一些默认参数的示例：

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
