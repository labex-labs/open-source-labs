# Create Data for Plotting

We will create data to plot using NumPy. We will generate 31 data points between -pi/2 and pi/2 and calculate the cosine of these values raised to the power of 3.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```
