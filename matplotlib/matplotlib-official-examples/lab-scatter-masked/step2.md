# Generating Data for the Scatter Plot

Next, we generate data for the scatter plot. We create 100 data points with random x and y values between 0 and 0.9, and random radii between 0 and 10. The color of each data point is determined by the square root of its area.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
```
