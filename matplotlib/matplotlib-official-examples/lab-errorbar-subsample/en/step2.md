# Plot All Errorbars

Next, we will plot all the error bars using the `errorbar` function without any subsampling. This will serve as our baseline plot.

```python
fig, ax = plt.subplots()

ax.set_title('All Errorbars')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
