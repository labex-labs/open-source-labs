# Add text to the plot

We will add text to the plot using the `ax.text()` function. We will add text to four different locations on the plot, each with a different font family: serif, monospace, sans-serif, and cursive.

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```
