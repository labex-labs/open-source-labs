# Plot something on the subplots

We will plot something on the subplots, so that the user can see the effect of the RectangleSelector and EllipseSelector.

```python
N = 100000  # If N is large one can see improvement by using blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # plot something
```
