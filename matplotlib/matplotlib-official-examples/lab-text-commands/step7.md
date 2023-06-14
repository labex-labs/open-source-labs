# Adding Annotations to the Plot

We can add annotations to the plot using the `ax.annotate()` function. This function takes three arguments: the annotation text, the xy-coordinate of the point to annotate, and the xy-coordinate of the text position. We can customize the annotation style using the `arrowprops` argument.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
