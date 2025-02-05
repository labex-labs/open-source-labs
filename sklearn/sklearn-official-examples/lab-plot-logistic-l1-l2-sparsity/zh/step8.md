# 设置标题和标签

我们将为子图设置标题和标签。

```python
    if i == 0:
        axes_row[0].set_title("L1 惩罚")
        axes_row[1].set_title("弹性网络\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("L2 惩罚")

    axes_row[0].set_ylabel("C = %s" % C)
```
