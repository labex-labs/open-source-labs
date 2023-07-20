# Simplest Hatched Plot with a Colorbar

In this step, we will create the simplest hatched plot with a colorbar. We will use the `contourf` function to create the filled contour plot and specify the hatches using the `hatches` parameter.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
