# Add the text box to the plot

Finally, we will add the text box to the plot using `matplotlib.pyplot.text()`. We will specify the location of the text box in axes coordinates and use the `bbox` parameter to add the box properties.

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
