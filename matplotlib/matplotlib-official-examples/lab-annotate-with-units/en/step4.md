# Add arrow annotation with unitized xy and text

In this step, we will add an arrow annotation to the plot using the `annotate()` function. We will provide the position of the arrow, the text to be displayed, and the arrow properties. We will also specify the units of measurement for the position and text.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
