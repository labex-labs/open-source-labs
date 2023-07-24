# Add Text to the Plot

You can add text to your plot using the `ax.text()` function. In this example, we will add text with different font families.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```
