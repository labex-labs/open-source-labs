# 导入 Matplotlib 并定义 on_close 函数

在这一步中，我们将导入 Matplotlib 并定义 `on_close` 函数，该函数将在图形关闭时被调用。该函数只会在控制台打印一条消息。

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
