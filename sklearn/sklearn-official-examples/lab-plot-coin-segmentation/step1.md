# Load and preprocess the image

We will start by loading the image of Greek coins and pre-processing it to make it easier to work with. We will resize the image to 20% of the original size and apply a Gaussian filter for smoothing prior to down-scaling to reduce aliasing artifacts.

```python
# load the coins as a numpy array
orig_coins = coins()

# Resize it to 20% of the original size to speed up the processing
# Applying a Gaussian filter for smoothing prior to down-scaling
# reduces aliasing artifacts.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
