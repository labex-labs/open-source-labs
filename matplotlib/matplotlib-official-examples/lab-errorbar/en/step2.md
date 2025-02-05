# Create example data

Next, we will create example data to use in the graph. In this example, we will use the `numpy.arange()` function to create an array of values between 0.1 and 4 with a step of 0.5. We will then use the `numpy.exp()` function to calculate the exponential of each value in the array.

```python
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
```
