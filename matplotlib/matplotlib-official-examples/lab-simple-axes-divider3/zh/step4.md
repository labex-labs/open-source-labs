# 自定义坐标轴范围和外观

我们将使用 `set_xlim`、`set_ylim` 和 `tick_params` 方法来自定义每个坐标轴的范围和外观。

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```
