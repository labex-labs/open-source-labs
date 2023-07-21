# Get Demo Image

In this step, we will define a function to get a demo image and its extent. We will be using `get_sample_data()` function from `cbook` to get a sample image.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
