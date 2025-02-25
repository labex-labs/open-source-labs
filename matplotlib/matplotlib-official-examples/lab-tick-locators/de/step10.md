# Den Log-Locator definieren

Der Log-Locator ist ein Locator, der Striche in regelmäßigen Abständen auf einer logarithmischen Skala platziert. Wir können den Log-Locator mit `ticker.LogLocator()` definieren.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
