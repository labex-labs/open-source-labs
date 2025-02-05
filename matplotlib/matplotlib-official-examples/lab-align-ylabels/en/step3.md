# Align Y-Labels Automatically

The third step is to align the y-labels automatically using the `.Figure.align_ylabels` method.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```
