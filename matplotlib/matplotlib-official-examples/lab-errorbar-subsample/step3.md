# Subsample Every 6th Errorbar

Now, let's apply errorbar subsampling to plot only every 6th error bar. We can do this by using the `errorevery` parameter of the `errorbar` function.

```python
fig, ax = plt.subplots()

ax.set_title('Every 6th Errorbar')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
