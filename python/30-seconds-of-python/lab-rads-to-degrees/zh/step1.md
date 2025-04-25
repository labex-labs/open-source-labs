# 弧度转角度

编写一个名为 `rads_to_degrees` 的 Python 函数，它接受一个参数 `rad`，这是一个表示弧度制角度的浮点数。该函数应以浮点数形式返回角度的度数。你可以使用以下公式将角度从弧度转换为度数：

```
degrees = radians * (180 / pi)
```

其中 `pi` 是一个常量值，表示圆的周长与其直径的比值，约等于 3.14159。

你的函数应从 `math` 模块中导入 `pi` 常量。

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
