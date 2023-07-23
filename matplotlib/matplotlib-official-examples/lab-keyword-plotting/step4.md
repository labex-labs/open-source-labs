# Generate Plot

In this step, we will generate a scatter plot using the `data` dictionary as input to the `scatter()` function. We will use the strings corresponding to the `a`, `b`, `c`, and `d` variables to generate the plot.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
```
