# Upsample Image with 'nearest' Interpolation

Now, we will upsample the image from 500 data pixels to 530 rendered pixels using 'nearest' interpolation. This will demonstrate how the Moiré patterns can still occur even when the image is upsampled if the upsampling factor is not an integer.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```
