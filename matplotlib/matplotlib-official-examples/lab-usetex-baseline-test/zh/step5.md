# 设置图表的范围和标签

我们将设置图表的范围和标签，以匹配预期的输出。

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
