# Create the Quiver Key

We can add a quiver key to the plot to show the scale of the arrows. We use the `ax.quiverkey()` function to add the key. We pass in the `q` object, the `X` and `Y` position of the key, the length of the arrow, the label for the key, and the position of the label.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```
