# Create a Scatter Plot

In this step, we will create a scatter plot using Matplotlib. We will start by generating some random data to plot using the NumPy `random()` function. Then, we will use the `scatter()` function to create the plot.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```
