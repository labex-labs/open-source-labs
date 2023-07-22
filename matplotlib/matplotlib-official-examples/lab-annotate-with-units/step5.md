# Add arrow annotation with mixed units

In this step, we will add another arrow annotation to the plot using the `annotate()` function. We will provide the position of the arrow, the text to be displayed, and the arrow properties. We will also mix units of measurement for the position and use the axes fraction for the text.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
