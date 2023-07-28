# Create Plot and Image

Next, we will create a plot and an image to show how to add a colorbar using inset axes.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```
