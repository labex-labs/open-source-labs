# Create the ImageGrids

We will create two ImageGrids to display our images. The first ImageGrid will have two rows and two columns, and the second ImageGrid will also have two rows and two columns.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
