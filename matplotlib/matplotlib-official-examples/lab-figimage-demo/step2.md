# Creating the figure and image

Next, we create the figure and the image that we want to place in it. In this example, we create a 100x100 array of random values and set the values in the right half of the image to 1. We then create two separate instances of the image, each with a different position and opacity.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
