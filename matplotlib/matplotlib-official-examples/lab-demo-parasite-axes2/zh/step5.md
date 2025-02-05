# 设置轴的范围和标签

我们将使用 `set()` 函数为每个轴设置 x 轴和 y 轴的范围及标签。

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
