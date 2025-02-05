# Grab frames and write to file

We loop through 100 iterations and generate random numbers for the x and y coordinates. We update the data for the line plot and grab the frame using the writer. Finally, we save the frames to a file.

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
