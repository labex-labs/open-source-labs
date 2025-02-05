# Add a Colorbar

Add a colorbar using the `colorbar` method. We will set the fraction and pad parameters to adjust the location of the colorbar, and set the label to show the name and units of the data.

```python
# Colorbar
fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')
```
