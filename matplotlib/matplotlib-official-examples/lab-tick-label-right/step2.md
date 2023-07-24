# Set the default y-axis tick labels on the right

We can set the default y-axis tick labels on the right side of the plot using the following code:

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
