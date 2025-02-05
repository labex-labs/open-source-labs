# Simple Picking, Lines, Rectangles, and Text

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
