# Add an Ellipse Patch with Hatching

You can also add hatched patches to your plot. In this case, we will be using the add_patch function to add an ellipse patch to our plot.

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```
