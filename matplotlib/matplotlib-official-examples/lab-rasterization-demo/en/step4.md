# Create a pcolormesh plot without rasterization

We will create a pcolormesh plot without rasterization to illustrate the difference between rasterization and non-rasterization.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
