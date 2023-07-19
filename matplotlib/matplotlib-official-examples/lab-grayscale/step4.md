# Defining the Image and Patch Example Function

We define the `image_and_patch_example` function that takes an axis object as input, plots a random image, and adds a patch to the plot.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
