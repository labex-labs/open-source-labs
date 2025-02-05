# Add Interactivity

When a point on the scatter plot is clicked, we want to plot the raw data from the dataset that generated that point. We will define a function `onpick` that will be called when a point is clicked. The function will plot the raw data and display the mean and standard deviation for that dataset.

```python
def onpick(event):

    if event.artist != line:
        return

    N = len(event.ind)
    if not N:
        return

    figi, axs = plt.subplots(N, squeeze=False)
    for ax, dataind in zip(axs.flat, event.ind):
        ax.plot(X[dataind])
        ax.text(.05, .9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    figi.show()


fig.canvas.mpl_connect('pick_event', onpick)
```
