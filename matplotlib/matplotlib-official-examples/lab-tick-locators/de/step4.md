# Den Multiple-Locator definieren

Der Multiple-Locator ist ein Locator, der Striche in regelmäßigen Abständen platziert. Wir können den Multiple-Locator mit `ticker.MultipleLocator()` definieren.

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
