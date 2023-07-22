# Load the image data

We will use an example image data called `bivariate_normal.npy` from `cbook` to demonstrate the ImageGrid. We load the image data using `get_sample_data` function from `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
