# Plot Variable, Symmetric Error Bars

We will now plot our data with variable, symmetric error bars. The `ax.errorbar()` function is used to create the plot, and the `yerr` parameter is used to specify the error values.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
