# スパインの位置を調整するメソッドを定義する

このステップでは、指定されたスパインの位置に基づいて軸のスパインの位置を調整するメソッドを定義します。

```python
def adjust_spines(ax, spines):
    """
    Adjusts the location of the axis spines based on the specified spine locations.

    Parameters:
        ax (Axes): The Matplotlib Axes object to adjust the spines for.
        spines (list of str): The desired spine locations. Valid options are 'left', 'right', 'top', 'bottom'.

    Returns:
        None
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # move the spine outward by 10 points
        else:
            spine.set_color('none')  # don't draw the spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
