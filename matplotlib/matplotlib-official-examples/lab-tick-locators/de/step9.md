# Den MaxN-Locator definieren

Der MaxN-Locator ist ein Locator, der eine maximale Anzahl von Strichen auf der Achse platziert. Wir können den MaxN-Locator mit `ticker.MaxNLocator()` definieren.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
