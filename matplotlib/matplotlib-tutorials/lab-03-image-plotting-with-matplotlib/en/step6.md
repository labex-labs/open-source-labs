# Array Interpolation Schemes

When resizing an image, it is necessary to interpolate the pixel values to fill the missing space. Different interpolation schemes can be used to determine the value of a pixel based on its surrounding pixels. Matplotlib provides different interpolation options, such as "nearest", "bilinear", and "bicubic".

```python
plt.imshow(img, interpolation="bilinear")
```
