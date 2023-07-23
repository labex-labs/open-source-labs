# Add the integral label

Add the integral label to the plot using `text`. The label should be centered at the midpoint between a and b and should be formatted using mathtext.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
