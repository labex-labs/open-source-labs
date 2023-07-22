# Perform Image Skew

In this step, we perform a skew of the image using the `skew_deg` function. We pass the skew angles as inputs to the `skew_deg` function. We use the `do_plot` function to display the skewed image.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
