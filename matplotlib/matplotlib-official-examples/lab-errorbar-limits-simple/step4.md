# Create the error bar plot with upper limits only

In this step, we create an error bar plot with only upper limits.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
