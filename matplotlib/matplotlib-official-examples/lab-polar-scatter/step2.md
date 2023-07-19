# Generate random data

We will generate random data for the scatter plot using NumPy. We will create 150 data points with random radius and angle values, and compute the area and color of each point.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
