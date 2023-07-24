# Add Subplots to the Inner GridSpec

We will now add subplots to the inner gridspec. We will create three subplots: `ax1`, `ax2`, and `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
