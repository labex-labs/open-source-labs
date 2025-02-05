# Perform Image Scale and Reflection

In this step, we perform a scale and reflection of the image using the `scale` function. We pass the scale and reflection factors as inputs to the `scale` function. We use the `do_plot` function to display the scaled and reflected image.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1, .5))
```
