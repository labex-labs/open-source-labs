# Prepare the sample data

We will use the `get_sample_data` function from cbook to obtain sample data. We will then prepare the images to be displayed in the grid.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
