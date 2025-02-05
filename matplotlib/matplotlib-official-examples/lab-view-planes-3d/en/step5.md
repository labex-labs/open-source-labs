# Create the 3D plot

We use `subplot_mosaic` to create the 3D plot based on the layout defined in step 4.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
