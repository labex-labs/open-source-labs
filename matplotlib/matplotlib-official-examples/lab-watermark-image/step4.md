# Overlay Image

To overlay the image on the plot, we can use the `figimage` method from the `matplotlib.figure.Figure` class. We need to specify the image, the position of the image on the plot, the z-order (to move the image to the front), and the alpha (to make the image semi-transparent).

```python
fig.figimage(im, 25, 25, zorder=3, alpha=.7)
```
