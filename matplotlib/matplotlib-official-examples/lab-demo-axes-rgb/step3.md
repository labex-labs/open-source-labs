# Define a function to create a RGB cube

In this step, we will define a function `make_cube()` to create a RGB cube from the R, G, and B channels obtained in the previous step. The function will return the R, G, and B cubes, as well as the RGB image.

```python
def make_cube(r, g, b):
    # Get the shape of R
    ny, nx = r.shape

    # Create the R, G, and B cubes
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Combine the R, G, and B cubes to create the RGB image
    RGB = R + G + B

    return R, G, B, RGB
```
