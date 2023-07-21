# Create a figure and two subplots

We will create a figure with two subplots using `subplots()` method. We will also set the projection to `'3d'` so that our subplots will be three-dimensional.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
