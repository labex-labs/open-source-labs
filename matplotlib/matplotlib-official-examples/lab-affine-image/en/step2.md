# Create a Function to Plot the Image

In this step, we define a function that takes the image, the plot axis, and the transformation as inputs. The function displays the image on the plot axis with the specified transformation. The function also displays a yellow rectangle around the image to show the intended extent of the image.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
