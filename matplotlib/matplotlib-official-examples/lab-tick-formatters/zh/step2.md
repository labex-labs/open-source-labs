# 简单格式化

在这一步中，我们将展示如何通过向 `~.Axis.set_major_formatter` 或 `~.Axis.set_minor_formatter` 传递字符串或函数来使用简单格式化器。我们将创建两个绘图，一个使用字符串格式化器，另一个使用函数格式化器。

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# 一个使用格式字符串函数语法的 ``str`` 可以直接用作格式化器。变量 ``x`` 是刻度值，变量 ``pos`` 是刻度位置。这会自动创建一个 StrMethodFormatter。
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# 一个函数也可以直接用作格式化器。该函数必须接受两个参数：用于刻度值的 ``x`` 和用于刻度位置的 ``pos``，并且必须返回一个 ``str``。这会自动创建一个 FuncFormatter。
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
