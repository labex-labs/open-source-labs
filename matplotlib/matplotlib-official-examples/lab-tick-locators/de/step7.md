# Den Index-Locator definieren

Der Index-Locator ist ein Locator, der Striche in regelmäßigen Abständen auf einer Indexskala platziert. Wir können den Index-Locator mit `ticker.IndexLocator()` definieren.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
