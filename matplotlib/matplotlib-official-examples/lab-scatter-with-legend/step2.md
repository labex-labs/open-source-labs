# Creating a Scatter Plot with Multiple Groups

We can create a scatter plot with multiple groups by looping through each group and creating a scatter plot for that group. We specify the color, size, and transparency of the markers for each group using the `c`, `s`, and `alpha` parameters, respectively. We also set the `label` parameter to the group name, which will be used in the legend.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
