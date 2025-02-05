# Perform Multiple Transformations

In this step, we perform multiple transformations of the image using the `rotate_deg`, `skew_deg`, `scale`, and `translate` functions. We pass the transformation parameters as inputs to the respective functions. We use the `do_plot` function to display the transformed image.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1, .5).translate(.5, -1))
```
