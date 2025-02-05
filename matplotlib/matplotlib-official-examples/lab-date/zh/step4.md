# 绘制数据

我们将使用 `plot` 函数在所有三个子图上绘制数据。

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')
```
