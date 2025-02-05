# Create Error Bars

In this step, we will create error bars on our polar axis. We will use the `errorbar()` function to create both radius and theta error bars.

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
