# Upsample Image with 'antialiased' Interpolation

Finally, we will upsample the image from 500 data pixels to 530 rendered pixels using 'antialiased' interpolation. This will demonstrate how using better antialiasing algorithms can reduce the Moiré patterns.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
