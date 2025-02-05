# Create the `Next` and `Previous` buttons

Now, we will create the `Next` and `Previous` buttons using `matplotlib.pyplot`'s `add_axes` function, and assign the callback functions we created earlier to them using `on_clicked`.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
