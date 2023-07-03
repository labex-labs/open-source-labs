# Tweak the Limits and Add Labels

Finally, we will tweak the limits of the plot and add axis labels using Matplotlib's `set_zlim()` and `set_xlabel()`, `set_ylabel()`, `set_zlabel()` functions. We will also use LaTeX math mode to write the axis labels.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
