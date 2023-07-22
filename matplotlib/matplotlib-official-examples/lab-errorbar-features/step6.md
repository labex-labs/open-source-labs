# Plot Log Scale with Error Bars

Finally, we will plot our data with a log scale and error bars. The `ax.set_yscale()` function is used to set the y-axis to a logarithmic scale.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
