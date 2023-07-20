# Adding the Legend

To add the legend to our plot, we use the `legend` function of Matplotlib. We pass in the `loc` parameter to specify the location of the legend, and the `shadow` parameter to add a shadow effect to the legend. We also use the `fontsize` parameter to set the font size of the legend.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```
