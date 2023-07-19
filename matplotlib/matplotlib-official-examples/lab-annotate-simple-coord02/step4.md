# Add Shape Annotation

Shapes can be used to draw attention to specific regions of a plot. In this step, we will add a rectangle to highlight the area between x=1 and x=3.

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
