# Scatter plot with round_numbers autolimit_mode

In this step, we will switch `axes.autolimit_mode` to 'round_numbers' and create a scatter plot to keep ticks at round numbers and also have ticks at the edges.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
