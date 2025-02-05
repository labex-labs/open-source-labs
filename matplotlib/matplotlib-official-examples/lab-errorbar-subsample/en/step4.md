# Shift Second Series by 3

In some cases, we may want to apply errorbar subsampling to different parts of our data. We can do this by specifying a tuple for the `errorevery` parameter. For example, let's apply errorbar subsampling to the second series, but shift it by 3 data points.

```python
fig, ax = plt.subplots()

ax.set_title('Second Series Shifted by 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
