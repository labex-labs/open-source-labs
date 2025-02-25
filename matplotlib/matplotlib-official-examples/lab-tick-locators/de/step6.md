# Den Linear-Locator definieren

Der Linear-Locator ist ein Locator, der Striche in regelmäßigen Abständen auf einer linearen Skala platziert. Wir können den Linear-Locator mit `ticker.LinearLocator()` definieren.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
