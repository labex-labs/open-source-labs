# Adding Horizontal Grid Lines

Finally, we will add horizontal grid lines to the box plots using the `yaxis.grid()` function.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```
