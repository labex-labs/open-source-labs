# Add Subplots to the Second Inner GridSpec

We will now add subplots to the second inner gridspec. We will create three subplots: `ax4`, `ax5`, and `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
