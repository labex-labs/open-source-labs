# Create the Plot

We create a 4x3 plot grid to show the hillshaded plots with different blend modes and vertical exaggeration. We first show the hillshade intensity image in the first row, and then place hillshaded plots with different blend modes in the rest of the rows. We use a for loop to iterate through the different vertical exaggeration values and blend modes.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay', 'soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
