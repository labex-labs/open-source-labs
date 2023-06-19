# Convert Image to Floats and Reshape

We will convert the image to floats and reshape it into a 2D numpy array so that it can be processed by the K-Means algorithm.

```python
# Convert to floats instead of the default 8 bits integer coding.
china = np.array(china, dtype=np.float64) / 255

# Get the dimensions of the image
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# Reshape the image into a 2D numpy array
image_array = np.reshape(china, (w * h, d))
```


