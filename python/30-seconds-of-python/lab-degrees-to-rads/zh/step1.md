# 度转弧度

编写一个函数 `degrees_to_rads(deg)`，它接受一个以度为单位的角度作为参数，并返回以弧度为单位的角度。你的函数应使用以下公式将度转换为弧度：

```
radians = (degrees * pi) / 180.0
```

其中 `pi` 是一个常量值，表示圆的周长与其直径的比值（约为3.14159）。

你的函数应以四舍五入到四位小数的弧度返回角度。

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
