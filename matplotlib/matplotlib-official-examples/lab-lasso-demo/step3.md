# Create the Plot

Now, use the `LassoManager` class to create an interactive plot. The `np.random.rand` function generates random data points that will be plotted.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```
