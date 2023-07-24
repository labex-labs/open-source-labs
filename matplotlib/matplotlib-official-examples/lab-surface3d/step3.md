# Create Data

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

We create the data for the plot. We create the `X` and `Y` values as arrays with evenly spaced values from -5 to 5 in increments of 0.25. We then create a meshgrid of `X` and `Y` values using `np.meshgrid()`. We use the meshgrid to calculate the `R` values, which is the distance from the origin. We then calculate the `Z` values using the `sin()` function of `R`.
