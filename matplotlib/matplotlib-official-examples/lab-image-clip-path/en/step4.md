# Create the Patch

To create the patch, we will use Matplotlib's `patches` module. We will create a circular patch with a radius of 200 pixels, centered at the point (260, 200).

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```
