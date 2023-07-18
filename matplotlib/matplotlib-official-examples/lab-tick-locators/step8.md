# Defining the Auto Locator

The auto locator is a locator that automatically places ticks at regular intervals. We can define the auto locator using `ticker.AutoLocator()`.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
