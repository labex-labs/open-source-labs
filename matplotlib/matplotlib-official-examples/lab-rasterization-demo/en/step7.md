# Create a pcolormesh plot with an overlaid text with rasterization

We will create a pcolormesh plot with an overlaid text with rasterization to illustrate how rasterization can enable vector graphics to maintain the advantages of vector graphics for some artists such as the axes and text.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
