# Create a Mercator Transform Scale Plot

As a bonus, we will also create a plot using the Mercator transform function. This is not a built-in function in Matplotlib, but we can define our own forward and inverse functions to create a Mercator transform scale plot. In this example, we will define the `forward()` and `inverse()` functions for the Mercator transform. We also add a title and grid to the plot.

```python
# Function Mercator transform
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
