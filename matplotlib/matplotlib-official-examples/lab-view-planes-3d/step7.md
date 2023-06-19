# Label each primary 3D view plane

We use the `annotate_axes` function defined in step 2 to label each primary 3D view plane with its respective angles.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
