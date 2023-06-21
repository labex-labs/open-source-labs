# Define the Animation Function

The sixth step is to define the animation function. This function will be called for each frame of the animation, and will update the position of the point on the left subplot, the position and data of the sine curve on the right subplot, and the position of the connection patch.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```

#
