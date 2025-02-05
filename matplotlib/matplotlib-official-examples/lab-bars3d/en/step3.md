# Generate Data for the Bar Graphs

We will now generate the data for the bar graphs. We will create four sets of data, each with 20 values. We will use the NumPy `arange()` method to create an array of 20 values and the NumPy `random.rand()` method to generate random values for each set of data.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
