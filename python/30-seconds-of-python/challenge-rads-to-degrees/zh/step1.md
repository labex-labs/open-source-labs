# 弧度转角度挑战

## 问题

编写一个名为 `rads_to_degrees` 的 Python 函数，它接受一个参数 `rad`，这是一个表示弧度角度的浮点数。该函数应以浮点数形式返回角度的度数。你可以使用以下公式将角度从弧度转换为度数：

```
度数 = 弧度 * (180 / π)
```

其中 `π` 是一个常量值，表示圆的周长与其直径的比值，约等于 3.14159。

你的函数应从 `math` 模块导入 `pi` 常量。

## 示例

以下是你的函数应如何工作的示例：

```python
from math import pi

assert rads_to_degrees(pi / 2) == 90.0
```
