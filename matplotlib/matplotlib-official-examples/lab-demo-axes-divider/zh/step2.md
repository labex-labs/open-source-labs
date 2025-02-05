# 获取示例图像

在这一步中，我们将定义一个函数来获取一张示例图像及其范围。我们将使用 `cbook` 中的 `get_sample_data()` 函数来获取一张示例图像。

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
