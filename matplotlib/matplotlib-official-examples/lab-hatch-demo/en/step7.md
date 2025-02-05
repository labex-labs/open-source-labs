# Add a Polygon Patch with Hatching

You can also add a polygon patch with hatching. In this case, we will be using the add_patch function to add a polygon patch to our plot.

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```
