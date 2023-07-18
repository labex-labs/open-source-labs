# Create a Custom Scale Plot

The final type of scale transformation we will explore is custom. This allows us to define our own forward and inverse functions for the scale transformation. In this example, we will define a custom function to take the square root of the data. To create a custom scale plot, we use the `set_yscale()` method and pass in the string `'function'`. We also define the `forward()` and `inverse()` functions and pass them as arguments to the `functions` parameter. We also add a title and grid to the plot.

```python
# Function x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
