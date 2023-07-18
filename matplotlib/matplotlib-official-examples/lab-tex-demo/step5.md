# Create a Bar Chart

In this step, we will create a bar chart using Matplotlib. We will start by generating some data to plot using the NumPy `random()` function. Then, we will use the `bar()` function to create the plot.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
