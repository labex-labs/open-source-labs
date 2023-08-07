# Plot the Histogram of MRI Intensity

Next, we will plot the histogram of MRI intensity using the `hist()` function. We will normalize the intensity values to range between 0 and 1.

```python
# Plot the histogram of MRI intensity
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Ignore the background
im = im / im.max()  # Normalize
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
```
