# Create a pcolormesh plot with an overlaid text without rasterization

We will create a pcolormesh plot with an overlaid text without rasterization to illustrate how vector graphics can maintain the advantages of vector graphics for some artists such as the axes and text.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
