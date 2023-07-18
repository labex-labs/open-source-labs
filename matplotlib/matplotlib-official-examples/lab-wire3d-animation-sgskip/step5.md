# Animate the Plot

The fifth step is to animate the plot. We will use a for loop to iterate through a range of values for phi. In each iteration, we will remove the previous line collection, generate new data, plot the new wireframe, and pause briefly before continuing.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
