# Matplotlib Picking Tutorial

## Introduction

This lab aims to introduce you to the concept of picking in Matplotlib. The ability to pick artists is a powerful tool that can be used to build interactive visualizations that respond to user actions. We will cover simple picking, picking with custom hit test functions, picking on a scatter plot, and picking images.

## Steps

### Step 1: Simple Picking, Lines, Rectangles, and Text

We will start by enabling simple picking by setting the "picker" property of an artist. This will enable the artist to fire a pick event if the mouse event is over the artist. We will create a simple plot containing a line, rectangle, and text, and enable picking on each of these artists.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Pick the rectangle.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Make the xtick labels pickable.
    label.set_picker(True)
```

### Step 2: Creating a Custom Hit Test Function

In this step, we will define a custom picker by setting picker to a callable function. The function will determine whether the artist is hit by the mouse event. If the mouse event is over the artist, we will return hit=True and props is a dictionary of properties you want added to the `.PickEvent` attributes.

```python
def line_picker(line, mouseevent):
    """
    Find the points within a certain distance from the mouseclick in
    data coords and attach some extra attributes, pickx and picky
    which are the data points that were picked.
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata)**2 + (ydata - mouseevent.ydata)**2)

    ind, = np.nonzero(d <= maxd)
    if len(ind):
        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()


def onpick2(event):
    print('onpick2 line:', event.pickx, event.picky)


fig, ax = plt.subplots()
ax.set_title('custom picker for line data')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)
```

### Step 3: Picking on a Scatter Plot

A scatter plot is backed by a `~matplotlib.collections.PathCollection`. We will create a scatter plot and enable picking.

```python
x, y, c, s = rand(4, 100)


def onpick3(event):
    ind = event.ind
    print('onpick3 scatter:', ind, x[ind], y[ind])


fig, ax = plt.subplots()
ax.scatter(x, y, 100*s, c, picker=True)
fig.canvas.mpl_connect('pick_event', onpick3)
```

### Step 4: Picking Images

Images plotted using `.Axes.imshow` are `~matplotlib.image.AxesImage` objects. We will create a figure with multiple images and enable picking.

```python
fig, ax = plt.subplots()
ax.imshow(rand(10, 5), extent=(1, 2, 1, 2), picker=True)
ax.imshow(rand(5, 10), extent=(3, 4, 1, 2), picker=True)
ax.imshow(rand(20, 25), extent=(1, 2, 3, 4), picker=True)
ax.imshow(rand(30, 12), extent=(3, 4, 3, 4), picker=True)
ax.set(xlim=(0, 5), ylim=(0, 5))


def onpick4(event):
    artist = event.artist
    if isinstance(artist, AxesImage):
        im = artist
        A = im.get_array()
        print('onpick4 image', A.shape)


fig.canvas.mpl_connect('pick_event', onpick4)
```

## Summary

In this lab, we learned how to enable picking on various artists in Matplotlib, including lines, rectangles, text, scatter plots, and images. We also learned how to define custom hit test functions to enable more complex picking behavior. This powerful tool allows us to create interactive visualizations that respond to user actions.
