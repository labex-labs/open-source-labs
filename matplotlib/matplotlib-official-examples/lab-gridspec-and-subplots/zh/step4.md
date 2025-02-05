# 移除底层轴

我们移除将在下一步创建的更大轴所覆盖的底层轴。

```python
for ax in axs[1:, -1]:
    ax.remove()
```
