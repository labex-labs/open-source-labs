# 定义图像数据

我们定义一个函数，该函数返回示例图像数据及其范围。

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
