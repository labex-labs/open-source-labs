# Create the error bar plot with both limits (default)

In this step, we create an error bar plot with both upper and lower limits, which is the default behavior.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
