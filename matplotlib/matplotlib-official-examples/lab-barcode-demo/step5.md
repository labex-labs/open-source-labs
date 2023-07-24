# Render the Barcode

Finally, we can render the barcode using `Axes.imshow`. We will use `code.reshape(1, -1)` to turn the data into a 2D array with one row, `imshow(..., aspect='auto')` to allow for non-square pixels, and `imshow(..., interpolation='nearest')` to prevent blurred edges.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
