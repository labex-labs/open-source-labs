# Defining the Linear Locator

The linear locator is a locator that places ticks at regular intervals on a linear scale. We can define the linear locator using `ticker.LinearLocator()`.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
