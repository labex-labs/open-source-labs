# Display the image and its histogram

Next, we will display the image using Matplotlib's `imshow` function, and its histogram using `hist`. We will create a figure with two subplots, one for the image and one for the histogram.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
