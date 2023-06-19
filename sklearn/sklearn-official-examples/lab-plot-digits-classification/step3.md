# Prepare the Dataset

We need to flatten the images to turn each 2-D array of grayscale values from shape `(8, 8)` into shape `(64,)`. This will give us a dataset of shape `(n_samples, n_features)`, where `n_samples` is the number of images and `n_features` is the total number of pixels in each image.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```


