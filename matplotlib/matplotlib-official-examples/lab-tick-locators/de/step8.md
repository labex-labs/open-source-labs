# Den Auto-Locator definieren

Der Auto-Locator ist ein Locator, der automatisch Striche in regelmäßigen Abständen platziert. Wir können den Auto-Locator mit `ticker.AutoLocator()` definieren.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
