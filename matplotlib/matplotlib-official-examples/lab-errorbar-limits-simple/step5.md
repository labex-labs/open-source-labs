# Create the error bar plot with both upper and lower limits

In this step, we create an error bar plot with both upper and lower limits.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
