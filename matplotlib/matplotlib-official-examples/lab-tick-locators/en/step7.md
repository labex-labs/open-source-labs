# Defining the Index Locator

The index locator is a locator that places ticks at regular intervals on an index scale. We can define the index locator using `ticker.IndexLocator()`.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
