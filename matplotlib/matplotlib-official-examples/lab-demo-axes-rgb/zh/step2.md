# 定义一个获取 RGB 通道的函数

在这一步中，我们将定义一个函数 `get_rgb()` 来获取图像的 R、G 和 B 通道。在这个例子中，我们将使用 `cbook` 模块的 `get_sample_data()` 函数来获取一个示例图像。

```python
import matplotlib.cbook as cbook

def get_rgb():
    # 获取一个示例图像
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # 获取 R、G 和 B 通道
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
