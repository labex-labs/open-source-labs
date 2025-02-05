# Define Update Function

We define a function that updates the plot for each frame of the animation. The function takes three inputs: `num` is the current frame number, `walks` is a list of all the random walks, and `lines` is a list of all the lines in the plot. For each line and walk, we update the data for the x, y, and z coordinates of the line up to the current frame number. We use `line.set_data()` and `line.set_3d_properties()` to update the x-y and z coordinates, respectively.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
