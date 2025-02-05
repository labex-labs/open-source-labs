# Extract the Renderer Buffer to a Numpy Array

The second option for saving the plot is to extract the renderer buffer to a numpy array. This allows us to use Matplotlib inside a cgi-script without needing to write a figure to disk. In this example, we will extract the renderer buffer and convert it to a numpy array.

```python
canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
