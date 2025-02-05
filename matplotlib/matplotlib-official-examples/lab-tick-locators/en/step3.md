# Defining the Null Locator

The null locator is a locator that does not place any ticks on the axis. We can define the null locator using `ticker.NullLocator()`.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
