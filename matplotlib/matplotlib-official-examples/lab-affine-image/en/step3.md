# Perform Image Rotation

In this step, we perform a rotation of the image using the `rotate_deg` function. We pass the rotation angle as the input to the `rotate_deg` function. We use the `do_plot` function to display the rotated image.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
