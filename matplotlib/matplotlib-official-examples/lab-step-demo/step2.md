# Create data for the plot

Next, let's create some data that we will use to plot. We will use the `numpy.arange()` function to create an array of values from 0 to 14 and store it in the variable `x`. We will also use the `numpy.sin()` function to create an array of values that are the sine of each value in `x` divided by 2, and store it in the variable `y`.

```python
x = np.arange(14)
y = np.sin(x / 2)
```
