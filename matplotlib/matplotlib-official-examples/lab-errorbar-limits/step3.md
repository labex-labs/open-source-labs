# Create Simple Error Bar Plot

We will create a simple error bar plot with standard error bars using the `errorbar` function. Here, we will set the x and y values along with their corresponding error values. We will also set the line style to dotted.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
