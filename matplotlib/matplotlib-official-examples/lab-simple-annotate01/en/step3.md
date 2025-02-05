# Add Text Annotation

We will now add a text annotation to the plot. The following code will add the text "Data Point 1" at the first data point.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
