# Set the font family

We will set the font family to "serif" using the `font.family` parameter. Additionally, we will set the `font.serif` parameter to an empty list to use the default LaTeX serif font.

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
