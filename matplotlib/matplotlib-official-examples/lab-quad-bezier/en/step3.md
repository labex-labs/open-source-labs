# Creating the PathPatch Object

Now that we have the `Path` object, we can create the `PathPatch` object that will be used to draw the Bezier Curve on the plot. We will set the `facecolor` to `'none'` so that only the curve is drawn and not filled.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
