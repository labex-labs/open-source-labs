# Create Line Segments

We will create a set of line segments so that we can color them individually. We will use the numpy `concatenate` function to concatenate two arrays `points[:-1]` and `points[1:]` along the second axis. We will then reshape the resulting array to an N x 1 x 2 array so that we can stack points together easily to get the segments. The segments array for line collection needs to be (numlines) x (points per line) x 2 (for x and y).

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
