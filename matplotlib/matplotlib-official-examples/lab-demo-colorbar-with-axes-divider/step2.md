# Create a plot

Next, we will create a plot using Matplotlib's `imshow` function. This function displays an image on the plot. We will also create a figure with two subplots.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
