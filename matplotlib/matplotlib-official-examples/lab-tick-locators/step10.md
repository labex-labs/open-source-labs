# Defining the Log Locator

The log locator is a locator that places ticks at regular intervals on a logarithmic scale. We can define the log locator using `ticker.LogLocator()`.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
