# Create PathPatch Object

In this step, we create a `PathPatch` object using the path object that we created in the previous step. This object is used to fill the area enclosed by the path. We can also set the color and transparency of the patch.

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```
