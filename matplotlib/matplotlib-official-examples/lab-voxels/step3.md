# Create the cubes and link

Now, we will create the two cubes and the link between them. We will do this by defining three boolean arrays that will be combined into a single boolean array. The first two arrays define the location of the cubes, while the third array defines the location of the link.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```
