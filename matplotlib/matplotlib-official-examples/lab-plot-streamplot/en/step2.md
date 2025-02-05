# Create Data

We will create the data for our streamplot using the Numpy library. In this example, we will create a meshgrid with 100 points in both directions and calculate the U and V components of our vector field.

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```
