# Defining the MaxN Locator

The MaxN locator is a locator that places a maximum number of ticks on the axis. We can define the MaxN locator using `ticker.MaxNLocator()`.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
