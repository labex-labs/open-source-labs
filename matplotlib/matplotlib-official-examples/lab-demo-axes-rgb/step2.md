# Define a function to get RGB channels

In this step, we will define a function `get_rgb()` to get the R, G, and B channels of an image. In this example, we will use the `get_sample_data()` function of the `cbook` module to get a sample image.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Get a sample image
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Get R, G, and B channels
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
