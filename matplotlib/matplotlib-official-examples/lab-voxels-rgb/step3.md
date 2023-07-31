# Creating the Sphere

We will now create a sphere in the plot by defining a condition for the RGB values that lie within a certain distance from the center of the plot.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
