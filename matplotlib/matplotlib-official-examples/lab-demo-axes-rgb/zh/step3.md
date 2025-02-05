# 定义一个创建 RGB 立方体的函数

在这一步中，我们将定义一个函数 `make_cube()`，用于根据上一步获得的 R、G 和 B 通道创建一个 RGB 立方体。该函数将返回 R、G 和 B 立方体以及 RGB 图像。

```python
def make_cube(r, g, b):
    # 获取 R 的形状
    ny, nx = r.shape

    # 创建 R、G 和 B 立方体
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # 合并 R、G 和 B 立方体以创建 RGB 图像
    RGB = R + G + B

    return R, G, B, RGB
```
