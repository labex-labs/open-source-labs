# Create a FigureCanvas and set the size request

```python
canvas = FigureCanvas(fig)
canvas.set_size_request(800, 600)
sw.set_child(canvas)
```

We create a FigureCanvas with the Matplotlib figure and set the size request to 800x600 pixels. We then set the FigureCanvas as the child of the ScrolledWindow.
