# Add Arrow Annotation

We will now add an arrow annotation to the plot. The following code will add an arrow from the first data point to the second data point.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
