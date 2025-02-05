# Creating the Circle

We will create the circle using the `make_circle()` function. The function takes the radius of the circle as input and returns the x and y coordinates of the circle.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
