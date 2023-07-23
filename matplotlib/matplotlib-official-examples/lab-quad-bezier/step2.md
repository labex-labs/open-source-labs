# Creating the Path

Next, we will create the `Path` object for the Bezier Curve. The `Path` object takes in a list of vertices and codes that specify the type of path between the vertices. In this case, we will use a `MOVETO` code to move to the starting point, followed by two `CURVE3` codes to specify the control points and ending point, and finally a `CLOSEPOLY` code to close the path.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
