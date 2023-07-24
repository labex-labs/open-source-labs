# Create a pcolormesh plot with rasterization

We will create a pcolormesh plot with rasterization to illustrate how rasterization can speed up rendering and produce smaller files.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
